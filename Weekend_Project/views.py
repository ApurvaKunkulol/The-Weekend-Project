from django.http import HttpResponse
import requests
from requests.packages.urllib3 import disable_warnings
import json
from .models import Article


def getarticles(request):   # retrieving all the articles from database.
    disable_warnings()
    output_articles = {}
    response = requests.get("https://community-hacker-news-v1.p.mashape.com/topstories.json?print=pretty", None,
                            headers={'X-Mashape-Key': '6n8esiDmEgmshvPdIJjg06nYp5PAp1fiP7jjsnD8lq7XjedUzN',
                            'Accept': 'application/json'})
    assert response.status_code == 200
    cnt = 10
    for repo in response.json():
        if cnt > 0:
            article = requests.get('https://community-hacker-news-v1.p.mashape.com/item/'+str(repo) +
                                   '.json?print=pretty', None,
                                   headers={'X-Mashape-Key': '6n8esiDmEgmshvPdIJjg06nYp5PAp1fiP7jjsnD8lq7XjedUzN',
                                            'Accept': 'application/json'}
                                   )
            output_articles.update({repo: article.json()})
            insertarticle(request, article.json())
            cnt -= 1
    response_str = json.dumps(output_articles)
    return HttpResponse(response_str)


def getsentiment(request, article_id=0):     # retrieving all the sentiment from database.
    disable_warnings()
    print "Inside the getsentiment function."
    article_set = Article.objects.filter(id=article_id)
    article_obj = article_set[0]
    print "Article retrieved from Database : ", article_obj.article_title.encode('utf-8')
    title = article_obj.article_title.encode('utf-8')
    res_sentiment = requests.get('https://twinword-sentiment-analysis.p.mashape.com/analyze/?text=' +
                                 title, None,
                                 headers={'X-Mashape-Key': '6n8esiDmEgmshvPdIJjg06nYp5PAp1fiP7jjsnD8lq7XjedUzN',
                                          'Accept': 'application/json'})
    sentiment = res_sentiment.json()
    print '\nResult Message : ', sentiment['result_msg'], '\nSentiment : ', sentiment['type']
    return HttpResponse('Sentiment : '+json.dumps(sentiment['type']))


def insertarticle(request, articles=None):
    print articles
    cnt = 10
    if articles is not None and cnt > 9:
        a = Article(article_author=articles['by'], article_title=articles['title'], article_URL=articles['url'],
                    article_score=articles['score'], article_sentiment='neutral')
        print "Article Author : ", a.article_author
        cnt -= 1
        try:
            a.save()
        except Exception, ex:
            print "Exception : ", ex.message