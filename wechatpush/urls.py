"""wechatpush URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from wechat.view.users import register, login, logout, user_center
from wechat.view.index import index
from wechat.view.user_center.user_info import user_info, change_info,notice
from wechat.view.wechat_group.publish_group import publish_group
from wechat.view.get_address import get_address
from wechat.views import test
from wechat.tests import create_profession,upload_image

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register),
    path('login/', login),
    path('logout/', logout),#退出
    path('index/', index),
    path('user_center/info/', user_center),#用户个人中心
    path('user_center/user_info/', user_info),#修改用户信息
    path('user_center/notice/', notice),#会员公告
    path('user_center/change_info/', change_info),  # 修改用户信息
    path('user_center/publish_group/', publish_group),  # 微信群发布
    path('upload/image/', publish_group),  # 上传图片


    path('select/join/', get_address),  # 获取地址
    # path('test/', create_profession),#创建行业表
    path('test/', upload_image),#创建行业表

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
