# -*- coding:utf-8 -*-
from django.contrib import admin
from board.models import *

class BoardAdmin(admin.ModelAdmin):
    list_display = ['name','description','article_count']
    inlines = []

    def article_count(self,obj):
        return Article.objects.filter(board=obj).count()
    article_count.short_description = u'총 글수'

class ArticleAdmin(admin.ModelAdmin):
    inlines = []
    date_hierarchy = 'reg_date'
    list_display = ['no','board','category','subject','user','reg_date']
    list_filter = ['board','category','is_announcement']


class CommentAdmin(admin.ModelAdmin):
    inlines = []


admin.site.register(Board,BoardAdmin)
admin.site.register(Article,ArticleAdmin)
admin.site.register(Comment,CommentAdmin)




