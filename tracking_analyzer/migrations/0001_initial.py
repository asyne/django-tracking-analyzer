# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-14 17:20
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tracker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('ip_address', models.GenericIPAddressField(blank=True, null=True)),
                ('ip_country', django_countries.fields.CountryField(blank=True, max_length=2)),
                ('ip_region', models.CharField(blank=True, max_length=255)),
                ('ip_city', models.CharField(blank=True, max_length=255)),
                ('referrer', models.URLField(blank=True)),
                ('device_type', models.CharField(choices=[('pc', 'PC'), ('mobile', 'Mobile'), ('tablet', 'Tablet'), ('bot', 'Bot'), ('unknown', 'Unknown')], default='unknown', max_length=10)),
                ('device', models.CharField(blank=True, max_length=30)),
                ('browser', models.CharField(blank=True, max_length=30)),
                ('browser_version', models.CharField(blank=True, max_length=30)),
                ('system', models.CharField(blank=True, max_length=30)),
                ('system_version', models.CharField(blank=True, max_length=30)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-timestamp',),
            },
        ),
    ]
