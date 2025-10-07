# 📚 Book Review System (Django Mini Project)

This is a simple Django-based mini project built for learning purposes. The goal of this project is to implement full CRUD operations using ModelForms, custom messages, dynamic URL routing, and Tailwind CSS for basic styling.

---

## 🚀 Features

- Add, edit, update, and delete book reviews
- ModelForms with custom widgets and CSS using Tailwind
- Success, error, and info messages using Django’s messaging framework
- Dynamic URL routing with `<int:pk>` for update and delete
- Template inheritance using `base.html`
- Error handling and validation messages

---

## 🛠️ Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML + Tailwind CSS
- **Database:** PostgreSQL

---

## 📂 Project Structure

Book_Review_System/
├── book/
│ ├── models.py
│ ├── views.py
│ ├── forms.py
│ ├── urls.py
│ └── templates/
│ └── ...
├── Book_Review_System/
│ ├── settings.py
│ └── urls.py
└── manage.py


---

## 🔧 How to Run Locally

1. **Clone the repo**  
   ```bash
   git clone https://github.com/Shivankitsingh3/Django_Learning_Projects/Book_Review_System.git
   cd Book_Review_System

2. Create virtual environment
  python -m venv .venv
  source venv/scripts/activate

3. Install dependencies
  pip install django
  pip install tailwindcss@latest
  pip install psycopg2

4. Run migrations
  python manage.py makemigrations
  python manage.py migrate

5. Start the Server 
  python manage.py runserver
