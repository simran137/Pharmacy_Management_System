# Generated by Django 2.1.7 on 2019-03-30 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_auto_20190330_1140'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='unit',
            name='unit',
        ),
    ]
