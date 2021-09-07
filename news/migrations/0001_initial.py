# Generated by Django 2.2 on 2021-09-07 01:49

import ckeditor.fields
import datetime
from django.db import migrations, models
import news.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=500, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=news.models.upload_location)),
                ('text', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('date_published', models.DateTimeField(default=datetime.datetime(2021, 9, 7, 1, 49, 58, 423837), verbose_name='date_published')),
                ('slug', models.SlugField(blank=True, unique=True)),
            ],
            options={
                'verbose_name': 'News',
                'verbose_name_plural': 'News',
            },
        ),
        migrations.CreateModel(
            name='PageTitleModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150, null=True)),
                ('page_promo', models.FileField(blank=True, null=True, upload_to=news.models.upload_location)),
            ],
            options={
                'verbose_name': 'Page Title',
                'verbose_name_plural': 'Page Title',
            },
        ),
    ]