# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-15 02:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ArtGallery', '0011_auto_20170914_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artwork',
            name='aw_img',
            field=models.ImageField(default='/static/images/profile-default.png', upload_to='artwork/1505443940.662818'),
        ),
    ]
