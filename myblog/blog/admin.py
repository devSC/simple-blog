# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from . import models


#super user : admin wilsonyuan
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'pub_time')
    list_filter = ('pub_time',)

# admin.site.register(models.Article)
admin.site.register(models.Article, ArticleAdmin)