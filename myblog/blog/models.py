# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


'''
修改完models中的任何属性后, 都需要再命令行中执行:

python manage.py makemigrations
python manage.py migrate
'''
class Article(models.Model):
    title = models.CharField(max_length=32, default='title')
    content = models.TextField(null=True)

    #创建对象时自动设置当前时间.
    pub_time = models.DateTimeField(null=True)

    def __str__(self):
        return self.title