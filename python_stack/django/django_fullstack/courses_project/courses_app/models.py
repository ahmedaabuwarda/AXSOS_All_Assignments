from django.db import models

# Create your models here.
class CourseManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}

        name = postData.get('name').strip()

        if (name == '' or name == None):
            errors['name.required'] = "Name field is Required!"
        
        if (len(name) < 5):
            errors['name.min'] = "Name field must be more than 5 characters!"

        return errors
    
class DiscriptionManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}

        desc = postData.get('desc').strip()

        if (desc == '' or desc == None):
            errors['desc.required'] = "Description field is Required!"

        if (len(desc) < 10):
            errors['desc.min'] = "Description field must be more than 10 characters!"

        return errors

class Course(models.Model):
    name = models.CharField(max_length=255, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = CourseManager()

class Discription(models.Model):
    course = models.OneToOneField(Course, related_name="description", on_delete=models.CASCADE)
    desc = models.CharField(max_length=255, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = DiscriptionManager()
