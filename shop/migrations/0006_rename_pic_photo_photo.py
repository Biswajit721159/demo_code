# Generated by Django 4.1.6 on 2023-02-17 05:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='pic',
            new_name='photo',
        ),
    ]
