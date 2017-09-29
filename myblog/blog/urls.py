#coding:utf8

__author__ = 'Wilson'


from django.conf.urls import url
from . import views
# 所有的Url
urlpatterns = [
    #配置blog/ 父路径下子路径的 请求响应的函数

    #空路径
    url(r'^$', views.index),
]
