# Generated by Django 4.1.7 on 2023-03-05 19:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webscraper', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='News',
            new_name='Events',
        ),
    ]
