# Generated by Django 2.1.7 on 2019-04-19 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0010_auto_20190418_1312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='MRP',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='item',
            name='discount',
            field=models.DecimalField(decimal_places=2, default=1.5, max_digits=4),
        ),
    ]