from django.contrib import admin

from todos.models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin) :
    list_display =['name', 'title', 'body', 'created']
    list_filter =['created']
