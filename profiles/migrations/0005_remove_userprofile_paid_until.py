# Generated by Django 3.1.3 on 2021-01-04 21:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_auto_20201228_0147'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='paid_until',
        ),
    ]
