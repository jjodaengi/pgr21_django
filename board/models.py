# -*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class Board(models.Model):

    class Meta:
        verbose_name = u'게시판'
        verbose_name_plural = u'게시판'

    def __unicode__(self):
        return self.description

    HTML_USE = (
        ('00',u'모두막기'),
        ('01',u'부분허용'),
        ('02',u'모두허용'),
        )

    name = models.CharField(max_length=10,verbose_name=u'게시판 아이디')
    description = models.CharField(max_length=40,verbose_name=u'게시판 설명')
    current_division = models.IntegerField(verbose_name=u'현재 division')

    article_per_page = models.IntegerField(default=20)
    page_per_view = models.IntegerField(default=10)
    page_top = models.TextField(null=True,blank=True)
    page_bottom = models.TextField(null=True,blank=True)

    use_html = models.CharField(choices=HTML_USE,max_length=2)
    use_fileupload = models.BooleanField(default=False,verbose_name=u'파일 업로드 기능 사용')
    use_sitelink = models.BooleanField(default=False,verbose_name=u'사이트 링크 기능 사용')
    use_secret = models.BooleanField(default=False,verbose_name=u'비밀글 기능 사용')
    use_category = models.BooleanField(default=False,verbose_name=u'카테고리 기능 사용')
    use_comment = models.BooleanField(default=True,verbose_name=u'댓글 기능 사용')

    total_upload_limit = models.IntegerField(default=0,verbose_name=u'전체 파일 업로드 용량')
    file_upload_limit = models.IntegerField(default=0,verbose_name=u'개별 파일 업로드 용량')

    #TODO: 커스텀 필드 - 콤마로 구분하는 텍스트 필드
    language_filter = models.TextField(null=True,blank=True)
    html_tag_filter = models.TextField(null=True,blank=True)
    ip_block_filter = models.TextField(null=True,blank=True)
    file_ext_filter = models.TextField(null=True,blank=True)


class Article(models.Model):

    def __unicode__(self):
        return self.board.description + ' ' + unicode(self.no) + u'번 글'

    class Meta:
        verbose_name = u'글'
        verbose_name_plural = verbose_name
    #dependencies
    no = models.IntegerField(default=0)
    board = models.ForeignKey(Board)
    memo = models.TextField(null=True)
    user = models.ForeignKey(User)
    password = models.CharField(max_length=20,null=True)
    name = models.CharField(max_length=40)
    ip = models.CharField(max_length=20,null=True)
    homepage = models.CharField(max_length=256,null=True)
    email = models.CharField(max_length=256,null=True)
    subject = models.CharField(max_length=250)
    use_html = models.BooleanField(default=False)
    reply_mail = models.BooleanField(default=False)
    category = models.IntegerField(default=0)
    is_secret = models.BooleanField(default=False)
    sitelink1 = models.CharField(max_length=256)
    sitelink2 = models.CharField(max_length=256)
    file_name1 = models.CharField(max_length=256)
    file_name2 = models.CharField(max_length=256)
    download1 = models.IntegerField(default=0)
    download2 = models.IntegerField(default=0)
    reg_date = models.DateTimeField(auto_now_add=True)
    hit = models.IntegerField(default=0)
    vote = models.IntegerField(default=0)
    total_comment = models.IntegerField(default=0)
    division = models.IntegerField(default=0)
    is_announcement = models.BooleanField(default=0,verbose_name=u'공지글')

class Comment(models.Model):
    class Meta:
        verbose_name = u'댓글'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.board.description + u' ' + unicode(self.article.no) + u'의 댓글'

    board = models.ForeignKey(Board)
    article = models.ForeignKey(Article)
    ismember = models.IntegerField(default=0)
    name = models.CharField(max_length=40)
    password = models.CharField(max_length=40)
    memo = models.TextField()
    ip = models.CharField(max_length=20)
    reg_date = models.DateTimeField(auto_now_add=True)

