# -*- coding:utf-8 -*-

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render_to_response

def index(request):
    #TODO : 데이터베이스 셋업 및 index.html 렌더링
    return render_to_response('index.html')
    pass



