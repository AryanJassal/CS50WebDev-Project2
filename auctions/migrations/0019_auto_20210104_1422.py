# Generated by Django 3.1 on 2021-01-04 03:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0018_bid_amount'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categories',
            old_name='category',
            new_name='name',
        ),
    ]