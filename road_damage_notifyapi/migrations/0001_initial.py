# Generated by Django 4.2 on 2023-05-01 20:42

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PotholeDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geo_location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('reported_at', models.DateTimeField(auto_now_add=True)),
                ('class_label', models.CharField(blank=True, choices=[('POTHOLED', 'potholed road'), ('UNPAVED', 'unpaved road')], max_length=20)),
                ('is_pothole_fixed', models.BooleanField(default=False)),
                ('is_informed', models.BooleanField(default=False)),
                ('state', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'PotholeDetails',
                'db_table': 'potholedetails',
            },
        ),
        migrations.CreateModel(
            name='StateRoadAuthority',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=200, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
            options={
                'verbose_name_plural': 'StateRoadAuthority',
                'db_table': 'state_road_authority',
            },
        ),
    ]
