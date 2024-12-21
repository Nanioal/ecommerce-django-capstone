# Authentication Setup and Testing Guide

This guide provides an overview of the authentication setup for the Django API project and instructions on how to test the implemented authentication endpoints.

## Setup Token Authentication

1. **Install Required Packages**
   Ensure that you have `djangorestframework` and `djangorestframework-authtoken` installed. You can install them using pip:
   ```bash
   pip install djangorestframework djangorestframework-authtoken
2. Add to Installed Apps Add 'rest_framework' and 'rest_framework.authtoken' to your INSTALLED_APPS in settings.py

3. Run Migrations Apply the migrations to create the necessary database tables
4. Configure DRF Settings Configure Django REST Framework (DRF) to use Token Authentication in settings.py

5. Create Token for Existing User Use the Django shell to create a token for an existing user

Testing Authentication Endpoints
6. Obtain Authentication Token
Using the following curl command to obtain an authentication token by providing the user's username and password : curl -X POST -H "Content-Type: application/json" -d '{"username":"yourusername", "password":"yourpassword"}' http://127.0.0.1:8000/api-token-auth/

7. Test Protected Endpoint (Create Category)