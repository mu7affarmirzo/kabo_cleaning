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
    file_path = 'files/news/{title}-{filename}'.format(
                title=str(instance.title), filename='{}.{}'.format(uuid4().hex, ext))
    return file_path


class PageTitleModel(models.Model):
    title = models.CharField(max_length=150, null=True, blank=True)
    page_promo = models.FileField(upload_to=upload_location, blank=True, null=True)

    def __str__(self):
        return self.title


class StatisticsModel(models.Model):
    title = models.CharField(max_length=150, null=True, blank=True)
    numbers = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return self.title


class MissionModel(models.Model):
    header = models.CharField(max_length=150, null=True, blank=True)
    title = models.CharField(max_length=150, null=True, blank=True)
    text = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to=upload_location, blank=True, null=True)

    def imageUrl(self):
        return self.image.url

    def __str__(self):
        return self.title
