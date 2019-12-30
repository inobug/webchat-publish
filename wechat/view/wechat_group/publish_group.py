from django.shortcuts import render, HttpResponse, redirect
from wechat.models import Profession,Topic,WechatGroup
from rest_framework.views import APIView
from utils.cirtys import CHINA_CIRTY

def publish_group(request):
    if request.method=='GET':

        china_cirty = CHINA_CIRTY.keys()
        professions=Profession.objects.all()
        topics=Topic.objects.all()
        return render(request, 'wechat_group/publish_group.html',
                      {'request': request, 'china_cirty': china_cirty,'professions':professions,'topics':topics})

    else:
        print(request.POST)
        profession=request.POST.get('type_id')
        topic=request.POST.get('topic_id')
        province_code=request.POST.get('province_code')
        city_code=request.POST.get('city_code')
        name=request.POST.get('name')
        id_description=request.POST.get('id_description')#介绍
        tags=request.POST.get('tags')
        wx_id=request.POST.get('wx_id')#群主wxid
        contact=request.POST.get('contact')#联系人
        mobile=request.POST.get('mobile')#电话
        qq=request.POST.get('qq')#qq

        return HttpResponse('ok')