# Generated by Django 2.2 on 2021-09-06 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='miniblockmodel',
            name='company_name_en',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='miniblockmodel',
            name='company_name_he',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='miniblockmodel',
            name='company_name_ru',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='miniblockmodel',
            name='name_en',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='miniblockmodel',
            name='name_he',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='miniblockmodel',
            name='name_ru',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='miniblockmodel',
            name='text_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='miniblockmodel',
            name='text_he',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='miniblockmodel',
            name='text_ru',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='portfoliomodel',
            name='company_name_en',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='portfoliomodel',
            name='company_name_he',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='portfoliomodel',
            name='company_name_ru',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='portfoliomodel',
            name='name_en',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='portfoliomodel',
            name='name_he',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='portfoliomodel',
            name='name_ru',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='portfoliomodel',
            name='text_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='portfoliomodel',
            name='text_he',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='portfoliomodel',
            name='text_ru',
            field=models.TextField(blank=True, null=True),
        ),
    ]