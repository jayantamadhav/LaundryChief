# Generated by Django 2.2.2 on 2019-07-09 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_auto_20190709_1533'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='items',
            name='status',
        ),
        migrations.AddField(
            model_name='customeritems',
            name='status',
            field=models.CharField(default='Not Cleaned', max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='salesmetrics',
            name='revenue_today',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='salesmetrics',
            name='revenue_total',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
