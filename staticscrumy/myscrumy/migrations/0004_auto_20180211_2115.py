# Generated by Django 2.0.1 on 2018-02-11 20:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myscrumy', '0003_auto_20180211_2114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scrumyuser',
            name='role_value',
            field=models.ForeignKey(default=700, on_delete=django.db.models.deletion.PROTECT, to='myscrumy.Rolez'),
        ),
        migrations.AlterField(
            model_name='status',
            name='status_id',
            field=models.IntegerField(default=700),
        ),
    ]