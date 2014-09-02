from django.db import models
from django.contrib import admin
from tinymce import models as tinymce_model

class Article(models.Model):
    id = models.AutoField(primary_key = True)
    title = models.CharField(max_length = 150)
    body = tinymce_model.HTMLField()
    timestamp = models.DateTimeField()

    class Meta():
        ordering = ('-timestamp',)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'timestamp')

admin.site.register(Article, ArticleAdmin)