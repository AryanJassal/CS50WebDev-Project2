# Generated by Django 3.1 on 2020-09-08 07:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_listing_indexdescription'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='whenMade',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
    ]
