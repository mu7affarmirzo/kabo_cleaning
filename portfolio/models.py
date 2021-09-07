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
    file_path = 'files/portfolio/{name}-{filename}'.format(
                name=str(instance.name), filename='{}.{}'.format(uuid4().hex, ext))
    return file_path


class PageTitleModel(models.Model):
    name = models.CharField(max_length=150, null=True, blank=True)
    page_promo = models.FileField(upload_to=upload_location, blank=True, null=True)
    image = models.ImageField(upload_to=upload_location, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Page Title'
        verbose_name_plural = 'Page Title'


class PortfolioModel(models.Model):
    company_name = models.CharField(max_length=500, blank=True, null=True)
    name = models.CharField(max_length=500, blank=True, null=True)
    image = models.ImageField(upload_to=upload_location, blank=True, null=True)
    text = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Portfolio'
        verbose_name_plural = 'Portfolio'


class MiniBlockModel(models.Model):
    root_project = models.ForeignKey(PortfolioModel, related_name='blocks', on_delete=models.CASCADE)
    name = models.CharField(max_length=500, blank=True, null=True)
    image = models.ImageField(upload_to=upload_location, blank=True, null=True)
    company_name = models.CharField(max_length=500, blank=True, null=True)
    text = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Portfolio blocks'
        verbose_name_plural = 'Portfolio blocks'
