# Generated by Django 3.1 on 2020-08-28 10:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_auto_20200824_1702'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='user',
            new_name='owner',
        ),
    ]