# -*- coding:utf-8 -*-

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext

def index(request):
    #TODO : 데이터베이스 셋업 및 base.html 렌더링
    return render_to_response('index.html',context_instance=RequestContext(request))



