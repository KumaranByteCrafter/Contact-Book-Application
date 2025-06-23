# Contact Book Application

A web-based contact management system built with **Django** and **Bootstrap**.  
Allows users to securely register, log in, and manage their contacts grouped by categories.  
Supports CSV import/export for bulk contact management with a responsive and user-friendly interface.

---

## 1. Features

- User Registration & Authentication  
- Add, Edit, Delete Contacts  
- Group contacts by categories (e.g., Family, Friends, Work)  
- Import and export contacts using CSV files  
- Responsive design using Bootstrap  

---

## 2. Technologies Used

- Python 3.9+  
- Django 4.2+  
- Bootstrap 5  
- SQLite (default database)  

---

## 3. Setup Instructions

### 3.1 Clone the repository

```bash
git clone <your-repo-url>
cd <your-project-folder>
```
### 3.2 Create and activate a virtual environment

```
python3 -m venv venv
source venv/bin/activate   # On Windows use: venv\Scripts\activate
```

### 3.3 Install dependencies

```
pip install -r requirements.txt
```

### 3.4 Apply migrations

```
python manage.py migrate
```

### 3.5 Create a superuser (admin)

```
python manage.py createsuperuser
```

## 3.6 Run the development server

```
python manage.py runserver
```
- Open your browser and visit: http://127.0.0.1:8000/

# 4. Usage

- Register a new user or login with existing credentials.
- Add contacts with details and assign them to categories.
- Export contacts to CSV for backup or sharing.
- Import contacts from CSV file via the import page.
# 5. Project Structure

```
contact_book/
│
├── contacts/               # Main app with models, views, templates
│   ├── migrations/         # Database migrations
│   ├── templates/contacts/ # HTML templates for the app
│   ├── admin.py            # Admin site config
│   ├── models.py           # Data models (Contact, Category, etc.)
│   ├── views.py            # Views for handling web requests
│   ├── urls.py             # App URL routing
│   └── forms.py            # Django forms (if any)
│
├── contact_book/           # Project settings and config
│
├── db.sqlite3              # SQLite database file
├── manage.py               # Django management script
├── requirements.txt        # Project dependencies
└── README.md               # This file
```
# 6. Contributing
- Feel free to fork this repo and submit pull requests.
- Please open issues for bugs or feature requests.
