# Authentication Setup

This guide provides a comprehensive overview of setting up and testing authentication in your Django project using JWT (JSON Web Tokens) with the `djangorestframework-simplejwt` package.

## Prerequisites

Ensure you have the following installed:

- Django
- Django REST Framework
- djangorestframework-simplejwt

If not, you can install them using pip:

```bash
pip install django djangorestframework djangorestframework-simplejwt
Configuration
1. Update settings.py
Add the necessary configurations for Django REST Framework and Simple JWT:

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
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'AUTH_HEADER_TYPES': ('Bearer',),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
}
2. Update urls.py
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
Usage
Obtain Token
Send a POST request to the /api/token/ endpoint with your username and password to obtain an access token and a refresh token.

Request:

bash
curl -X POST http://localhost:8000/api/token/ -d "username=YOUR_USERNAME&password=YOUR_PASSWORD"
Response:

json
{
    "refresh": "your_refresh_token",
    "access": "your_access_token"
}
Use Access Token
Include the obtained access token in the Authorization header to make authenticated requests to your API endpoints.

Example Request:

bash
curl -X GET http://localhost:8000/api/users/ -H "Authorization: Bearer your_access_token"
Refresh Token
Send a POST request to the /api/token/refresh/ endpoint with your refresh token to obtain a new access token.

Request:

bash
curl -X POST http://localhost:8000/api/token/refresh/ -d "refresh=your_refresh_token"
Response:

json
{
    "access": "new_access_token"
}
Testing Authentication
Using Django Shell
To retrieve all users and inspect their IDs:

Open the Django shell:

bash
python manage.py shell
Run the following Python commands:

python
from store.models import User

users = User.objects.all()
for user in users:
    print(f"ID: {user.id}, Username: {user.username}")
Example Endpoints
List Users
URL: /api/users/

Method: GET

Authorization: Bearer Token

Create User
URL: /api/users/create_user/

Method: POST

Request Body:

json
{
    "username": "string",
    "password": "string",
    "email": "string"
}
Sign In User
URL: /api/users/sign_in_user/

Method: POST

Request Body:

json
{
    "username": "string",
    "password": "string"
}
