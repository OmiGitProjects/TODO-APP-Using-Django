# Generated by Django 3.0.6 on 2020-06-05 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_auto_20200605_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tododatabase',
            name='task_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
