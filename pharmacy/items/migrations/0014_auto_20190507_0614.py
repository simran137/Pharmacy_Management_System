# Generated by Django 2.2.1 on 2019-05-07 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0013_remove_item_concentration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='type',
            field=models.CharField(choices=[('tablet', 'tablet'), ('capsule', 'capsule'), ('injection', 'injection'), ('pouch', 'pouch'), ('bottle', 'bottle'), ('cream', 'cream'), ('gel', 'gel'), ('other', 'other')], max_length=15),
        ),
    ]