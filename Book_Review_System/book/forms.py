from django import forms
from book.models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'title', 'author', 'description', 'genre', 'isbn', 'publication_date'
        ]
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:border-blue-500',
                    'placeholder': 'Enter book title'
                }
            ),
            'author': forms.TextInput(
                attrs={
                    'class': 'w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:border-blue-500',
                    'placeholder': 'Enter author name'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:border-blue-500',
                    'rows': 4,
                    'placeholder': 'Enter book description'
                }
            ),
            'genre': forms.Select(
                attrs={
                    'class': 'w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:border-blue-500',
                }
            ),
            'isbn': forms.TextInput(
                attrs={
                    'class': 'w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:border-blue-500',
                    'placeholder': 'Enter ISBN'
                }
            ),
            'publication_date': forms.DateInput(
                attrs={
                    'class': 'w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:border-blue-500',
                    'type': 'date'
                }
            ),
        }
