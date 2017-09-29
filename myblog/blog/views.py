# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from . import models

# Create your views here.


#处理请求
def index(request):
    article = models.Article.objects.get(pk=1)
    return render(request, 'blog/index.html', {'article' : article})



