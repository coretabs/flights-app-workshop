# Generated by Django 3.0.2 on 2020-02-01 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0002_auto_20200201_1519'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flight',
            name='date',
        ),
        migrations.AlterField(
            model_name='flight',
            name='to_time',
            field=models.TimeField(),
        ),
    ]
