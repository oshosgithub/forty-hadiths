# Generated by Django 4.2.5 on 2023-09-16 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
