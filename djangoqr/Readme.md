---

### ✅ **2. djangoqr – README.md**


# 🔳 Django QR Code Generator

This is a Django-based web app that allows users to generate QR codes for any text or URL input. The project is simple and focuses on learning Django forms, views, and third-party integrations.

---

## 🚀 Features

- Generate QR codes for any input text or URL
- Download the QR code as an image
- Simple and clean UI using Tailwind CSS

---

## 🛠️ Tech Stack

- **Backend:** Django (Python)
- **QR Code Generation:** `qrcode` Python package
- **Frontend:** HTML + Tailwind CSS
- **Database:** PostgreSQL

---

## 📂 Project Structure

djangoqr/
├── core/
│ ├── views.py
│ ├── forms.py
│ ├── templates/
│ └── urls.py
├── djangoqr/
│ ├── settings.py
│ └── urls.py
├── scan/
│ ├── views.py
│ ├── forms.py
│ ├── templates/
│ └── urls.py
└── manage.py

---

## 🔧 How to Run Locally

1. **Clone the repo**  
   ```bash
   git clone https://github.com/Shivankitsingh3/Django_Learning_Projects/djangoqr.git
   cd djangoqr

2. Create virtual environment
  python -m venv venv
  source .venv/scripts/activate


3. Install dependencies
  pip install django
  pip install qrcode
  pip install psycopg2
  pip install pillow
  pip install tailwindcss@latest


4. Run migrations
  python manage.py makemigrations
  python manage.py migrate


5. Run the server 
  python manage.py runserver
