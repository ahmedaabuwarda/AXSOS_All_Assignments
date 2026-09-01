from django.db import models

# Create your models here.
class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}

        title = postData.get('title').strip()
        network = postData.get('network').strip()
        release_date = postData.get('release_date').strip()
        desc = postData.get('desc').strip()

        # title
        if (title == '' or title == None):
            errors['title.required'] = "Title field is Required!"

        if (len(title) < 2):
            errors['title.min'] = "Title field must be at least 2 characters"

        title_matches = Show.objects.filter(title__iexact=title)
        if postData.get('show_id'):
            title_matches = title_matches.exclude(id=postData.get('show_id'))

        if title_matches.exists():
            errors['title.unique'] = "Title already exists!"

        # network
        if (network == '' or network == None):
            errors['network.required'] = "Network field is Required!"

        if (len(network) < 3):
            errors['network.min'] = "Network field must be at least 3 characters"

        # description
        if (desc == '' or desc == None):
            errors['desc.required'] = "Description field is Required!"

        if (len(desc) < 10):
            errors['desc.min'] = "Description field must be at least 3 characters"

        # release_date
        if (release_date == '' or release_date == None):
            errors['release_date.required'] = "Released Date field is Required!"

        if (len(release_date) < 10):
            errors['release_date.min'] = "Released Date field must be at least 3 characters"

        return errors


class Show(models.Model):
    title = models.CharField(max_length=255, default=None)
    network = models.CharField(max_length=255, default=None)
    release_date = models.DateTimeField()
    desc = models.TextField(default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()
