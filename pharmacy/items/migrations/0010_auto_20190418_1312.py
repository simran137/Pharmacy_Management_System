# Generated by Django 2.1.7 on 2019-04-18 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0009_auto_20190413_0359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='discount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4),
        ),
    ]
