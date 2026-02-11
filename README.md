# 🛒 Django Storefront

A mini e-commerce backend built using **Django** and **Django REST Framework**.  
This project supports products, collections, cart, checkout, authentication, and REST APIs.

---

## 🚀 Features

- Product & Collection management
- Product detail pages using slugs
- Cart functionality (add, update, remove items)
- Checkout & order creation
- User authentication (login / logout)
- Orders linked to authenticated users
- REST APIs for products, collections, and orders
- Clean modular Django app structure

---

## 🧰 Tech Stack

- Python 3
- Django
- Django REST Framework
- MySQL
- HTML (Django Templates)
- Git & GitHub

---

## 📂 Project Structure

Project - Django Tutorial
storefront/
├── storefront/ # Project settings
├── store/ # Main app
│ ├── views/
│ │ ├──__init__.py
│ │ ├── cart.py
│ │ ├── checkout.py
│ │ ├── collections.py
│ │ |── home.py
| | └── products.py
│ ├──__init__.py
│ ├── admin.py
│ ├── api_urls.py
│ ├── api_views.py
│ ├── apps.py
│ ├── models.py
│ ├── serializers.py
│ ├── tests.py
│ └── urls.py
├── templates/ 
│    ├──registration
│    │   └──login.html
│    ├──store
│    │   ├──base.html
│    │   ├──cart.html
│    │   ├──checkout_success.html
│    │   ├──collection_detail.html
│    │   ├──collection_list.html
│    │   ├──product_detail.html
│    │   └──product_list.html
├──tags       
├──.gitignore
├──db.sqlite3
├── manage.py
└── README.md


---

## 🔑 Authentication

Uses Django’s built-in authentication system.

Available routes:
- `/accounts/login/`
- `/accounts/logout/`

Checkout is protected — only logged-in users can place orders.

---

## 🌐 API Endpoints

### Products
- `GET /api/products/`
- `GET /api/products/<slug>/`

### Collections
- `GET /api/collections/`

### Orders (Authenticated)
- `GET /api/my-orders/`

---

## ▶️ How to Run Locally

```bash
# Create virtual environment
python -m venv env
env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Migrate database
python manage.py makemigrations
python manage.py migrate

# Create admin user
python manage.py createsuperuser

# Run server
python manage.py runserver




#URLs
http://127.0.0.1:8000/admin/auth/user/
http://127.0.0.1:8000/     # For now home page is products list
