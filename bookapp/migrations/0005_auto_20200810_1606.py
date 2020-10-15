# Generated by Django 3.0.8 on 2020-08-10 10:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0004_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='uid',
        ),
        migrations.AddField(
            model_name='customer',
            name='udestination',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='ulocation',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='utype',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
