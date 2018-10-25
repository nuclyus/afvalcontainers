# Generated by Django 2.1.2 on 2018-10-25 13:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('afvalcontainers', '0011_auto_20181003_0747'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteFractieStat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fractie', models.CharField(max_length=20)),
                ('week', models.IntegerField(blank=True, null=True)),
                ('year', models.IntegerField(blank=True, null=True)),
                ('wegingen', models.IntegerField(blank=True, null=True)),
                ('sum', models.IntegerField(blank=True, null=True)),
                ('min', models.IntegerField(blank=True, null=True)),
                ('max', models.IntegerField(blank=True, null=True)),
                ('avg', models.IntegerField(blank=True, null=True)),
                ('stddev', models.IntegerField(blank=True, null=True)),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='afvalcontainers.Site', to_field='short_id')),
            ],
        ),
    ]
