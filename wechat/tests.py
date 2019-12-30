from django.test import TestCase
from django.shortcuts import render, HttpResponse, redirect

# Create your tests here.

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'wechat',
        'HOST': '132.232.38.103',
        'PORT': '3306',
        'USER': 'root',
        'PASSWORD': 'XIAzhen5@1',
    }
}
from wechat.models import Profession
s="""

微商,
互粉群,
招代理商,
免费赚钱,
创业群,
代理品牌,
公众号开发,
微营销,
萌宠,
摄影群,
旅游,
运动,
购物,
母婴群,
汽车,
美食,
宝妈群,
    淘宝优惠券,
粉丝互动,
时尚交友,
美女模特,
互赞群,
驴友群,
车友群,
吃喝玩乐,
交朋友,
影视娱乐,
爱音乐,
动漫娱乐,
吃鸡手游,
全民K歌群,
众筹,
手游群,
网游群,
英雄联盟群,
王者荣耀群,
微信投票群,
土豪群,
股票交流群,
投资交流群,
美女直播,
聊天群,
8090,
职业群,
人脉群,
网络红人,
其他,
    微信小程序,
    
"""
def create_profession(request):
    ss=s.split(',')
    for i in ss :
        if i :
            p=Profession(profession=i)
            p.save()
    return HttpResponse('ok')


def upload_image(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        avatar = request.FILES.get('avatar')

        with open(avatar.name, 'wb') as f:
            for line in avatar:
                f.write(line)
        return HttpResponse('ok')

    return render(request, 'test.html')