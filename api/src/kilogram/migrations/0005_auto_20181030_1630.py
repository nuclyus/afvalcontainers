# Generated by Django 2.1.2 on 2018-10-30 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kilogram', '0004_auto_20181030_1622'),
    ]

    operations = [
        migrations.AddField(
            model_name='buurtfractiestatmonth',
            name='containers',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='buurtfractiestatweek',
            name='containers',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
