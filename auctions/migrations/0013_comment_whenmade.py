# Generated by Django 3.1 on 2020-09-22 09:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0012_comment_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='whenMade',
            field=models.DateTimeField(default=datetime.datetime.now, editable=False),
        ),
    ]
