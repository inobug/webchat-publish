from django.shortcuts import render, HttpResponse,redirect
from django.contrib import auth

from rest_framework.views import APIView
from wechat.models import User
from wechat.pro_serializer.user_serializer import CreateUsersRequestSerializer


class Users(APIView):
    def get(self, request):
        pass

    def post(self, request):

        return HttpResponse('ok')


class ModifyUser(APIView):
    def put(self, request):
        pass

    def delete(self, request):
        pass


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    if request.method == 'POST':
        print(request.POST)
        email = request.POST.get('Email')
        phone = request.POST.get('PhoneNum')
        username = request.POST.get('LoginName')
        password = request.POST.get('Password')
        repeat_password = request.POST.get('ConfirmPassword')
        pet_name = request.POST.get('DisplayName')
        if not username:
            return HttpResponse('用户名不能为空')
        if not password:
            return HttpResponse('密码不能为空')
        if not repeat_password:
            return HttpResponse('确认密码不能为空')

        if username and password and repeat_password:
            if password == repeat_password:
                # filter() 函数用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表
                user_project = User.objects.filter(username=username).first()
                if user_project:
                    return HttpResponse('用户名已存在')
                else:
                    User.objects.create_user(username=username, password=password,pet_name=pet_name,phone=phone,email=email).save()
                    return redirect('/login/')
            else:
                return HttpResponse('两次输入的密码不一致')
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        username = request.POST.get('user')
        password = request.POST.get('pwd')
        print(username)
        print(password)
        users=User.objects.all()
        for k in users:
            print(k.username,k.username,k.password)
        user = auth.authenticate(username=username, password=password)
        print(user)
        if user:
            auth.login(request, user)
            return HttpResponse('1')
        else:
            return HttpResponse('0')
    return render(request, 'login.html')
def logout(request):
    auth.logout(request)
    return redirect('/index/')
def user_center(request):
    return render(request,'center_user.html',locals())