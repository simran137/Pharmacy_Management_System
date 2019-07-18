# Generated by Django 2.1.7 on 2019-03-22 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('address', models.CharField(max_length=150)),
                ('email_id', models.EmailField(max_length=50)),
                ('phone_no', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Login_db',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=70)),
                ('password', models.CharField(max_length=70)),
                ('role', models.CharField(max_length=10)),
            ],
        ),
    ]
