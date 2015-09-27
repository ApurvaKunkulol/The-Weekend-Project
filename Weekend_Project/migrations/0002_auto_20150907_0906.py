# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Weekend_Project', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='article_URL',
        ),
        migrations.RemoveField(
            model_name='article',
            name='article_author',
        ),
        migrations.RemoveField(
            model_name='article',
            name='article_score',
        ),
        migrations.RemoveField(
            model_name='article',
            name='article_sentiment',
        ),
        migrations.RemoveField(
            model_name='article',
            name='article_title',
        ),
    ]
