# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-02 17:34
from __future__ import unicode_literals

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('image', models.ImageField(storage=django.core.files.storage.FileSystemStorage(location='/static/img/'), upload_to=b'')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
