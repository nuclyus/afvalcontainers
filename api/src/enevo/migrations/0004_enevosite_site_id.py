# Generated by Django 2.1.5 on 2019-01-30 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enevo', '0003_auto_20190114_1445'),
    ]

    operations = [
        migrations.AddField(
            model_name='enevosite',
            name='site_id',
            field=models.IntegerField(db_index=True, null=True),
        ),
    ]