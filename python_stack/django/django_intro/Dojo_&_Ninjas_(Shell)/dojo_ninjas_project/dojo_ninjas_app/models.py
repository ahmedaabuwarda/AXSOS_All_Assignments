from django.db import models

# Create your models here.
class Dojo(models.Model):
    name = models.CharField(max_length=255, default=None)
    city = models.CharField(max_length=255, default=None)
    state = models.CharField(max_length=2, default=None)
    desc = models.CharField(max_length=255, default='')
    created_at = models.DateTimeField(auto_now_add=True)


class Ninja(models.Model):
    dojo = models.ForeignKey(Dojo, related_name="ninjas", on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, default=None) 
    last_name = models.CharField(max_length=255, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
