# Generated by Django 2.0.1 on 2018-04-03 12:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myscrumy', '0011_remove_status_status_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scrumyuser',
            name='password',
        ),
    ]