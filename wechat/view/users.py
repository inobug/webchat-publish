from django.shortcuts import render, HttpResponse,redirect

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
        username = request.POST.get('请输入用户名')
        password = request.POST.get('请输入密码')
        repeat_password = request.POST.get('请输入确认密码')
        pet_name = request.POST.get('请输入昵称')
        if not username:
            return HttpResponse('用户名不能为空')
        if not password:
            return HttpResponse('密码不能为空')
        if not repeat_password:
            return HttpResponse('确认密码不能为空')
        if username and password and repeat_password:
            if password == repeat_password:
                # filter() 函数用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表
                user_project = User.objects.filter(user_name=username).first()
                if user_project:
                    return HttpResponse('用户名已存在')
                else:
                    User.objects.create(user_name=username, password=password,pet_name=pet_name).save()
                    return redirect('/login/')
            else:
                return HttpResponse('两次输入的密码不一致')
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        username = request.POST.get('请输入用户名')
        password = request.POST.get('请输入密码')
        user_project = User.objects.filter(user_name=username).first()
        if user_project and user_project.password==password:
            return redirect('/index/')
        else:
            return  HttpResponse('用户名或者密码错误')

