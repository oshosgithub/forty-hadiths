# Generated by Django 4.2.5 on 2023-09-16 06:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_profile_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
    ]
