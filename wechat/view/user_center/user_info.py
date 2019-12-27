from django.shortcuts import render, HttpResponse,redirect

from rest_framework.views import APIView
from wechat.models import User

def user_info(request):
    if request.method == 'GET':
        return render(request,'user_center/user_info.html',locals())