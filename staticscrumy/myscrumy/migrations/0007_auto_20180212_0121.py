# Generated by Django 2.0.1 on 2018-02-12 00:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myscrumy', '0006_auto_20180211_2120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scrumyuser',
            name='role_value',
            field=models.ForeignKey(default=11, on_delete=django.db.models.deletion.PROTECT, to='myscrumy.Rolez'),
        ),
    ]