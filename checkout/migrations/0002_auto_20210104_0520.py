# Generated by Django 3.1.3 on 2021-01-04 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment_intent',
            field=models.CharField(default='', max_length=254),
        ),
        migrations.AddField(
            model_name='order',
            name='payment_method',
            field=models.CharField(default='', max_length=254),
        ),
    ]
