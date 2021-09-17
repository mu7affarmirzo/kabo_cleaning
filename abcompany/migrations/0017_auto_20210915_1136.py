# Generated by Django 2.2 on 2021-09-15 06:36

import abcompany.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abcompany', '0016_auto_20210915_1127'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancymodel',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
        migrations.AlterField(
            model_name='vacancymodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=abcompany.models.vacancy_upload_location),
        ),
    ]