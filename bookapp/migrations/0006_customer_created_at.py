# Generated by Django 3.0.8 on 2020-08-13 06:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0005_auto_20200810_1606'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='created_at',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
