

from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100)
    bio= models.TextField(max_length=300)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']  # Make sure this list doesn't include 'email'

    def __str__(self):
        return self.username
