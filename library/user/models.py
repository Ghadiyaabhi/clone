from django.db import models
from django.contrib.auth.models import User
from management.models import Book

class forgotpassword(models.Model):
      email = models.EmailField(default=True)

def __str__(self):
    return self.email
     

