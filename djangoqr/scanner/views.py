from django.shortcuts import render
from scanner.models import QRCode
import qrcode
from django.core.files.storage import FileSystemStorage
from io import BytesIO
from django.core.files.base import ContentFile
from django.conf import settings
from pathlib import Path
from pyzbar.pyzbar import decode
from PIL import Image
import os  # for path operations

# Create your views here.


def generate_qr(request):
    qr_image_url = None
    if request.method == 'POST':
        mobile_number = request.POST.get('mobile_number')
        data = request.POST.get('qr_data')

        # Validating the mobile number
        if not mobile_number or len(mobile_number) != 10 or not mobile_number.isdigit():
            return render(request, 'scanner/generate.html', {'error': 'Invalid mobile number'})

        # Generate the QR code image with data and mobile number
        qr_content = f"{data}|{mobile_number}"

        qr_img = qrcode.make(qr_content)

        qr_image_io = BytesIO()  # Creating a BytesIO stream

        # Save the QR Code image to qr_image_io with png format
        qr_img.save(qr_image_io, format='PNG')

        qr_image_io.seek(0)  # Reset the position of the stream

        # Define the storage location for the QR code images
        # Using os.path.join for building paths
        qr_storage_path = os.path.join(settings.MEDIA_ROOT, 'qr_codes')
        fs = FileSystemStorage(location=qr_storage_path,
                               base_url='/media/qr_codes/')

        filename = f"{data}_{mobile_number}.png"
        qr_image_content = ContentFile(qr_image_io.read(), name=filename)
        # fs.save handles existing files
        fs.save(filename, qr_image_content)
        qr_image_url = fs.url(filename)

        # Save the QR code data and mobile number in the database
        QRCode.objects.create(data=data, mobile_number=mobile_number)

    return render(request, 'scanner/generate.html', {'qr_image_url': qr_image_url})


def scan_qr(request):
    result = None
    if request.method == 'POST' and request.FILES.get('qr_image'):

        mobile_number = request.POST.get('mobile_number')
        qr_image = request.FILES['qr_image']

        # Validating the mobile number
        if not mobile_number or len(mobile_number) != 10 or not mobile_number.isdigit():
            return render(request, 'scanner/scan.html', {'error': 'Invalid mobile number'})

        # Save the uploaded image temporarily
        fs = FileSystemStorage()
        filename = fs.save(qr_image.name, qr_image)
        image_path = Path(fs.location) / filename

        try:
            # For decoding it
            image = Image.open(image_path)
            decoded_objects = decode(image)

            if decoded_objects:
                # Get data from first decoded object
                qr_content = decoded_objects[0].data.decode('utf-8').strip()

                if '|' not in qr_content:
                    result = "Scan Failed: The QR code format is invalid."
                else:
                    qr_data, qr_mobile_number = qr_content.split('|')

                    # The .first() method is for QuerySets, not strings.
                    qr_entry = QRCode.objects.filter(
                        data=qr_data, mobile_number=qr_mobile_number).first()

                    if qr_entry and qr_mobile_number == mobile_number:
                        result = "Scan Success: Valid QR Code. Payment processed."

                        # Delete the specific qr code entry from the database
                        qr_entry.delete()

                        # Delete the original qr code image from the media/qr_codes directory
                        # Using os.path.join for building the path
                        original_qr_image_path = Path(os.path.join(
                            settings.MEDIA_ROOT, 'qr_codes', f"{qr_data}_{qr_mobile_number}.png"))

                        if original_qr_image_path.exists():
                            original_qr_image_path.unlink()  # Deletes the original QR code image

                    else:
                        result = "Scan Failed: Invalid QR Code or mobile number mismatch."
            else:
                result = "No QR Code detected in the image."
        except Exception as e:
            result = f"Error processing the image: {str(e)}"
        finally:
            # it ensures that the uploaded temporary image is always deleted
            if image_path.exists():
                image_path.unlink()

    return render(request, 'scanner/scan.html', {'result': result})
