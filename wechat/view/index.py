from django.shortcuts import render, HttpResponse,redirect

from rest_framework.views import APIView
from wechat.models import User
from wechat.pro_serializer.user_serializer import CreateUsersRequestSerializer

def index(request):
    print(request.user.username)
    print(request.user.pet_name)
    return render(request,'index.html',locals())