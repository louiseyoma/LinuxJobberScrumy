# Generated by Django 2.0.1 on 2018-02-12 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myscrumy', '0007_auto_20180212_0121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scrumygoals',
            name='task_id',
            field=models.IntegerField(default=700),
        ),
    ]
