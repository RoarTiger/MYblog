#-*- coding: utf-8 -*-
from django.db import models

class Category(models.Model):
    CateName = models.CharField(max_length=20, verbose_name='类名')
    Articles = models.IntegerField(verbose_name='文章数')

    class Meta:
        db_table = '分类'

class Article(models.Model):
    title = models.CharField(max_length=30, verbose_name='文章标题')
    date = models.DateField(verbose_name='发表时间')
    readers = models.IntegerField(default=0, verbose_name='阅读量')
    likes = models.IntegerField(default=0, verbose_name='赞')
    content = models.TextField(verbose_name='文章内容')
    ArticleCategory = models.ManyToManyField(Category, verbose_name='分类')

    class Meta:
        db_table = '文章'