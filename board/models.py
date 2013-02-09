from django.db import models
from django.contrib.auth.models import User

class Board(models.Model):
    name = models.CharField(max_length=10)

class Article(models.Model):
    #dependencies
    board = models.ForeignKey(Board)

    no = models.AutoField()
    memo = models.TextField(null=True)
    ip = models.CharField(max_length=20,null=True)

    password = models.CharField(max_length=20,null=True)
    user = models.ForeignKey(User)
    name = models.CharField(max_length=40)
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

class Comment(models.Model):
    board = models.ForeignKey(Board)
    article = models.ForeignKey(Article)
    ismember = models.IntegerField(default=0)
    name = models.CharField(max_length=40)
    password = models.CharField(max_length=40)
    memo = models.TextField()
    ip = models.CharField(max_length=20)
    reg_date = models.DateTimeField(auto_now_add=True)

