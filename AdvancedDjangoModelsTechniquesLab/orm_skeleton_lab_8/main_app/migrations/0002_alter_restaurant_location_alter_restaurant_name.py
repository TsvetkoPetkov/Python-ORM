# Generated by Django 4.2.4 on 2023-11-22 13:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='location',
            field=models.CharField(max_length=200, validators=[django.core.validators.MinLengthValidator(2, 'Location must be at least 2 characters long.'), django.core.validators.MaxLengthValidator(200, 'Location cannot exceed 200 characters.')]),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='name',
            field=models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(2, 'Name must be at least 2 characters long.'), django.core.validators.MaxLengthValidator(100, 'Name cannot exceed 100 characters')]),
        ),
    ]
