# -*- coding: utf-8 -*-
# Create your views here.
from django.template import loader, Context
from django.shortcuts import render_to_response
from django.http import HttpResponse
from articles.models import Article

def articles(request):
    return render_to_response('articles.html', {'articles': Article.objects.all()})

def article(request, article_id = 2):
    return render_to_response('article.html',
                              {'article': Article.objects.get(id = article_id)}
                            )