from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from .models import *

# Create your views here.

ARTICLES_PER_PAGE=10

def blog(request):
    articles = Article.objects.order_by('-date_time') # -field means descending
    hide_next = len(articles) <= ARTICLES_PER_PAGE
    hide_prev = True
    context = {'articles': articles[:ARTICLES_PER_PAGE], 'articleview': False, 'currentpage': '0', 'hide_next': hide_next, 'hide_prev': hide_prev}
    return render(request, 'blog/blog.html', context)

def blogpage(request, pagenum):
    pagenum=int(pagenum)
    if pagenum==0:
        return blog(request)
    articles = Article.objects.order_by('-date_time') # -field means descending
    shown_articles = articles[(pagenum*ARTICLES_PER_PAGE):(pagenum+1)*ARTICLES_PER_PAGE]
    hide_next = not ((pagenum+1)*ARTICLES_PER_PAGE < len(articles))
    hide_prev = False
    context = {'articles': shown_articles,
        'articleview': False, 'currentpage': pagenum, 'hide_next': hide_next, 'hide_prev': hide_prev}
    return render(request, 'blog/blog.html', context)

def article(request, articleid):
    article = get_object_or_404(Article, id=articleid)
    context = {'articles': [article], 'articleview': True}
    return render(request, 'blog/blog.html', context)
