# Generated by Django 2.0.1 on 2018-02-11 20:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myscrumy', '0004_auto_20180211_2115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scrumygoals',
            name='time_of_status_change',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]