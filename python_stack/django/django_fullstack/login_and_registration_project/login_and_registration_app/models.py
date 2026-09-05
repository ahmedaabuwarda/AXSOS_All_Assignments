import re

from django.db import models

# Create your models here.
class UserManager(models.Manager):
    def register_validator(self, postData):

        errors = {}

        if (postData['first_name'] == '' or postData['first_name'] == None):
            errors["first_name.required"] = "First name field is required!"
        if len(postData['first_name']) < 2:
            errors["first_name.min"] = "First name should be at least 2 characters"
        if len(postData['last_name']) < 2:
            errors["last_name.min"] = "Last name should be at least 2 characters"

        if (postData['email'] == '' or postData['email'] == None):
            errors["email.required"] = "Email field is required!"
        if len(postData['email']) < 5:
            errors["email.min"] = "Email should be at least 5 characters"
        if (postData['email'] and not re.match(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$', postData['email'])):
            errors["email.email"] = "Invalid email address" 

        if (postData['password'] == '' or postData['password'] == None):
            errors["password.required"] = "Password field is required!"
        if len(postData['password']) < 8:
            errors["password.min"] = "Password should be at least 8 characters"
        if postData['password'] != postData['confirm_password']:
            errors["confirm_password"] = "Passwords do not match"


        return errors

    def login_validator(self, postData):
        errors = {}

        if (postData['email'] == '' or postData['email'] == None):
            errors["email.required"] = "Email field is required!"
        if len(postData['email']) < 5:
            errors["email.min"] = "Email should be at least 5 characters"
        if (postData['email'] and not re.match(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$', postData['email'])):
            errors["email.email"] = "Invalid email address" 

        if (postData['password'] == '' or postData['password'] == None):
            errors["password.required"] = "Password field is required!"
        if len(postData['password']) < 8:
            errors["password.min"] = "Password should be at least 8 characters"

        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = UserManager()