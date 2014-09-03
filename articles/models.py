# -*- coding: utf-8 -*-
from django.db import models
from django.contrib import admin
from tinymce import models as tinymce_model

class Article(models.Model):
    id = models.AutoField(primary_key = True)
    title = models.CharField(max_length = 150, verbose_name=u'Заголовок')
    body = tinymce_model.HTMLField(verbose_name=u'Текст статьи')
    timestamp = models.DateTimeField(verbose_name=u'Дата/Время публикации')

    class Meta():
        ordering = ('-timestamp',)
        verbose_name = u'Публикация'
        verbose_name_plural = u'Публикации'

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'timestamp')

admin.site.register(Article, ArticleAdmin)