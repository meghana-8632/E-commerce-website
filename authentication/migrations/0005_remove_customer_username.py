# Generated by Django 3.2.13 on 2022-07-26 06:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_customer_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='username',
        ),
    ]
