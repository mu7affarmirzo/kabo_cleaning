# Generated by Django 2.2 on 2021-09-15 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abcompany', '0020_vacancymodel_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancymodel',
            name='slug',
            field=models.SlugField(blank=True, default=1, unique=True),
            preserve_default=False,
        ),
    ]
