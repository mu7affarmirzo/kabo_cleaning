# Generated by Django 2.2 on 2021-09-03 05:21

import abcompany.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abcompany', '0010_auto_20210903_0519'),
    ]

    operations = [
        migrations.AddField(
            model_name='companymissionmodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=abcompany.models.upload_location),
        ),
    ]
