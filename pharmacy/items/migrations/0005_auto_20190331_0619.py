# Generated by Django 2.1.7 on 2019-03-31 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0004_auto_20190331_0559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]
