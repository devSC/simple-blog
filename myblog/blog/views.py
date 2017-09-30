# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from . import models

# Create your views here.


#处理请求
def index(request):
    #获取所有文章
    articles = models.Article.objects.all()
    return render(request, 'blog/index.html', {'articles' : articles})


def article_page(request, article_id):
    article = models.Article.objects.get(pk = article_id)
    return render(request, 'blog/article_page.html', {'article' : article})

def edit_page(request, article_id):
    if str(article_id) == '0':
        return render(request, 'blog/edit_page.html')
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'blog/edit_page.html', {'article' : article})



def edit_action(request):
    title = request.POST.get('title', 'TITLE') #TITLE 为默认值.
    content = request.POST.get('content', 'CONTENT')
    article_id = request.POST.get('article_id', 0)

    if str(article_id) == '0':
        models.Article.objects.create(title=title, content=content)
        articles = models.Article.objects.all()
        return render(request, 'blog/index.html', {'articles': articles})

    #修改旧数据
    article = models.Article.objects.get(pk = article_id)
    article.title = title
    article.content = content
    article.save()
    return render(request, 'blog/article_page.html', {'article' : article})
