# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-01 19:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MusicHistoryAPI', '0002_auto_20170201_1845'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='album_release_date',
            field=models.DateField(default='2012-01-01'),
        ),
        migrations.AddField(
            model_name='album',
            name='album_title',
            field=models.CharField(default='SOME STRING', max_length=128),
        ),
        migrations.AddField(
            model_name='artist',
            name='artist_name',
            field=models.CharField(default='SOME STRING', max_length=128),
        ),
        migrations.AddField(
            model_name='genre',
            name='genre_name',
            field=models.CharField(default='SOME STRING', max_length=128),
        ),
        migrations.AddField(
            model_name='song',
            name='song_length',
            field=models.CharField(default='SOME STRING', max_length=128),
        ),
        migrations.AddField(
            model_name='song',
            name='song_release_date',
            field=models.DateField(default='2012-01-01'),
        ),
        migrations.AddField(
            model_name='song',
            name='song_title',
            field=models.CharField(default='SOME STRING', max_length=128),
        ),
    ]