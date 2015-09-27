from django.db import models


class Article(models.Model):
    article_author = models.CharField(max_length=500, default='unknown')
    article_title = models.CharField(max_length=500, default='unknown')
    article_URL = models.CharField(max_length=1000, default='www.google.com')
    article_score = models.IntegerField(default=0)
    article_sentiment = models.CharField(max_length=50, default='neutral')

    #def __str__(self):
    #    return self



# Create your models here.
