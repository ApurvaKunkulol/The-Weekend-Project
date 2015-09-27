# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('article_author', models.CharField(max_length=500)),
                ('article_title', models.CharField(max_length=500)),
                ('article_URL', models.CharField(max_length=1000)),
                ('article_score', models.IntegerField()),
                ('article_sentiment', models.CharField(max_length=50)),
            ],
        ),
    ]
