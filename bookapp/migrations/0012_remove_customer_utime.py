# Generated by Django 3.0.8 on 2020-09-20 19:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0011_customer_utime'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='utime',
        ),
    ]
