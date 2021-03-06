# Generated by Django 3.1 on 2021-01-15 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0025_auto_20210106_1520'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bid',
            options={'ordering': ['-amount']},
        ),
        migrations.AlterModelOptions(
            name='categories',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='listing',
            options={'ordering': ['-timestamp']},
        ),
        migrations.AlterField(
            model_name='listing',
            name='categories',
            field=models.ManyToManyField(blank=True, null=True, to='auctions.Categories'),
        ),
    ]
