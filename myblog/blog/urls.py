#coding:utf8

__author__ = 'Wilson'


from django.conf.urls import url
from . import views
# 所有的Url
urlpatterns = [
    #配置blog/ 父路径下子路径的 请求响应的函数

    #空路径
    url(r'^$', views.index),
    #文章路径 已 article_id 抓取 id
    url(r'^article/(?P<article_id>[0-9]+)$', views.article_page, name='article_page'),
    url(r'^edit/(?P<article_id>[0-9]+)$', views.edit_page, name='edit_page'),
    url(r'^edit_action/$', views.edit_action, name='edit_action')
]
