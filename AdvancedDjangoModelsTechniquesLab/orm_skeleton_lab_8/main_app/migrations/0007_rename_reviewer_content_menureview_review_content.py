# Generated by Django 4.2.4 on 2023-11-22 17:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_alter_foodcriticrestaurantreview_options_menureview'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menureview',
            old_name='reviewer_content',
            new_name='review_content',
        ),
    ]
