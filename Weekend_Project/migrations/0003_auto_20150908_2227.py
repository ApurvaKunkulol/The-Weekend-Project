# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Weekend_Project', '0002_auto_20150907_0906'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_URL',
            field=models.CharField(default=b'www.google.com', max_length=1000),
        ),
        migrations.AddField(
            model_name='article',
            name='article_author',
            field=models.CharField(default=b'unknown', max_length=500),
        ),
        migrations.AddField(
            model_name='article',
            name='article_score',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='article',
            name='article_sentiment',
            field=models.CharField(default=b'neutral', max_length=50),
        ),
        migrations.AddField(
            model_name='article',
            name='article_title',
            field=models.CharField(default=b'unknown', max_length=500),
        ),
    ]
