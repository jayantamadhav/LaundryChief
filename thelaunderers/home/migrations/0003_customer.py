# Generated by Django 2.2.2 on 2019-06-29 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_remove_customuser_full_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cust_name', models.CharField(max_length=100)),
                ('cust_email', models.EmailField(max_length=254)),
            ],
        ),
    ]
