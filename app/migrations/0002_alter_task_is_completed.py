# Generated by Django 3.2.23 on 2023-11-05 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='is_completed',
            field=models.BooleanField(default=False),
        ),
    ]