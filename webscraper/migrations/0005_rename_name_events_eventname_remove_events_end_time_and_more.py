# Generated by Django 4.1.7 on 2023-03-06 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webscraper', '0004_alter_events_link'),
    ]

    operations = [
        migrations.RenameField(
            model_name='events',
            old_name='name',
            new_name='eventname',
        ),
        migrations.RemoveField(
            model_name='events',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='events',
            name='start_time',
        ),
        migrations.AddField(
            model_name='events',
            name='date_and_time',
            field=models.CharField(default='default', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='events',
            name='organization',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='events',
            name='placeid',
            field=models.CharField(default='', max_length=200),
        ),
    ]