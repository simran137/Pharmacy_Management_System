# Generated by Django 2.1.7 on 2019-03-23 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='role',
            field=models.CharField(choices=[('Admin', 'Admin'), ('Worker', 'Worker')], default='Worker', max_length=10),
        ),
        migrations.AlterField(
            model_name='login_db',
            name='role',
            field=models.CharField(choices=[('Admin', 'Admin'), ('Worker', 'Worker')], default='Worker', max_length=10),
        ),
    ]
