# Generated by Django 2.2.2 on 2019-07-12 20:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20190709_1556'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='added_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
