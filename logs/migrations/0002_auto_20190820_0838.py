# Generated by Django 2.2.4 on 2019-08-20 08:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='log',
            old_name='day',
            new_name='date',
        ),
    ]
