# Generated by Django 3.0.6 on 2020-06-05 10:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tododatabase',
            name='timeStamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
