# Generated by Django 2.1.7 on 2019-03-30 11:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item_to_unit',
            old_name='Discount',
            new_name='discount',
        ),
    ]
