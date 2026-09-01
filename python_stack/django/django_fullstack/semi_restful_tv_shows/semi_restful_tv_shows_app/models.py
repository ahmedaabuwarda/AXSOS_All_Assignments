from django.db import models

# Create your models here.
class Show(models.Model):
    title = models.CharField(max_length=255, default=None)
    network = models.CharField(max_length=255, default=None)
    release_date = models.DateTimeField()
    desc = models.TextField(default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)