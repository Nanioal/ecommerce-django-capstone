markdown
# Django E-Commerce Product API Project

## Overview

This project is a Django-based e-commerce platform that provides a seamless online shopping experience. It includes features such as product browsing, order management, user authentication, reviews, and wishlists.

## Features

- User authentication with JWT
- Product management
- Order management
- User profiles
- Reviews and ratings
- Wishlists
- Search and filter functionality

## Setup Instructions

### Prerequisites

- Python 3.6+
- Django 3.0+
- PostgreSQL (or SQLite for local development)

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
Create a Virtual Environment

bash
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
Install Dependencies

bash
pip install -r requirements.txt
Configure the Database

Update the DATABASES setting in your settings.py file to configure your database. For local development, you can use SQLite:

python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / "db.sqlite3",
    }
}
For production, use PostgreSQL or another database of your choice.

Apply Migrations

bash
python manage.py makemigrations
python manage.py migrate
Create a Superuser

bash
python manage.py createsuperuser
Run the Development Server

bash
python manage.py runserver
Authentication Setup
This project uses JWT for authentication. To set up JWT authentication, follow these steps:

Add JWT Configuration in settings.py

python
INSTALLED_APPS = [
    ...
    'rest_framework',
    'rest_framework_simplejwt.token_blacklist',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'AUTH_HEADER_TYPES': ('Bearer',),
}
Update urls.py

Add the token endpoints to your project's urls.py:

python
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include('store.urls')),  # Replace 'store' with your app name
]
API Endpoints
Obtain Token
URL: /api/token/

Method: POST

Request Parameters:

json
{
    "username": "string",
    "password": "string"
}
Response:

json
{
    "refresh": "string",
    "access": "string"
}
Refresh Token
URL: /api/token/refresh/

Method: POST

Request Parameters:

json
{
    "refresh": "string"
}
Response:

json
{
    "access": "string"
}
Testing
To run the tests, use the following command:

bash
python manage.py test
