# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-25 18:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0002_campaignresponse'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='image',
            field=models.ImageField(blank=True, upload_to='img/%y/%m/%d'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='pic',
            field=models.ImageField(blank=True, upload_to='img/user'),
        ),
    ]
