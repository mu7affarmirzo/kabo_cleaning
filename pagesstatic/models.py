from django.db import models
from ckeditor.fields import RichTextField
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.dispatch import receiver
from django.db.models.signals import post_delete
from uuid import uuid4

import random as r


def upload_location(instance, filename):
    ext = filename.split('.')[-1]
    file_path = 'about/{name}-{filename}'.format(
                name=str(instance.name), filename='{}.{}'.format(uuid4().hex, ext))
    return file_path


class LeadersModel(models.Model):
    name = models.CharField(max_length=500, null=True, blank=True)
    position = models.CharField(max_length=500, null=True, blank=True)
    image = models.ImageField(upload_to=upload_location, null=True, blank=True)

    class Meta:
        ordering = ['-name']

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    def __str__(self):
        return str(self.name)

