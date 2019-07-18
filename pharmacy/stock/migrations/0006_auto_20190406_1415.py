# Generated by Django 2.1.7 on 2019-04-06 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0005_auto_20190405_0825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='batch_no',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='stock',
            name='item_id',
            field=models.ForeignKey(on_delete=[('', '---------')], to='items.Item'),
        ),
    ]