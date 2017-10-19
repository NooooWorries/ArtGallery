# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-12 04:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ArtGallery', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='auctionrecord',
            old_name='ar_deadline',
            new_name='ar_expiration',
        ),
        migrations.RenameField(
            model_name='auctionrecord',
            old_name='ar_time',
            new_name='ar_startTime',
        ),
        migrations.AlterField(
            model_name='artwork',
            name='aw_img',
            field=models.ImageField(default='/static/images/profile-default.png', upload_to='artwork/1507783569.6457138'),
        ),
        migrations.AlterField(
            model_name='auctionrecord',
            name='ar_isEnd',
            field=models.BooleanField(default=False),
        ),
    ]
