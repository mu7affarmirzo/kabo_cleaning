# Generated by Django 2.2 on 2021-09-07 08:38

from django.db import migrations, models
import news.models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20210907_0446'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagetitlemodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=news.models.upload_location),
        ),
    ]