# Generated by Django 2.1.2 on 2018-11-01 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kilogram', '0005_auto_20181030_1630'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitefractiestatmonth',
            name='capacity',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sitefractiestatweek',
            name='capacity',
            field=models.FloatField(blank=True, null=True),
        ),
    ]