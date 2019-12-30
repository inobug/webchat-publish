from django.shortcuts import render, HttpResponse, redirect

from rest_framework.views import APIView
from wechat.models import User
from utils.cirtys import CHINA_CIRTY


def change_str(s):
    if len(s) == 1:
        s = '0' + s
    return s


def user_info(request):
    if request.method == 'GET':
        china_cirty = CHINA_CIRTY.keys()
        print(china_cirty)
        cirty = request.user.area
        if cirty:
            c = cirty.split('-')
            province_code = c[0]
            city_code = c[-1]
            already_cirty = CHINA_CIRTY[province_code]
        else:
            province_code = ''
            city_code = ''
            already_cirty = []

        year = [i for i in range(1960, 2011)]
        month = [i for i in range(1, 13)]
        day = [i for i in range(1, 32)]
        return render(request, 'user_center/user_info.html',
                      {'request': request, 'china_cirty': china_cirty, 'city_code': city_code,
                       'province_code': province_code, 'already_cirty': already_cirty, 'year': year, 'month': month,
                       'day': day})


def change_info(request):
    if request.method == 'POST':
        print(request.POST)
        id = request.POST.get('id')
        name = request.POST.get('name')
        year = request.POST.get('year')
        month = change_str(request.POST.get('month'))
        day = change_str(request.POST.get('day'))

        province_code = request.POST.get('province_code')
        city_code = request.POST.get('city_code')

        user = User.objects.get(pk=id)
        if user:
            brithday = year + '-' + month + '-' + day
            city = province_code + '-' + city_code
            user.brithday = brithday
            user.area = city
            user.pet_name = name
            user.save()
        return redirect('/user_center/user_info/')


def notice(request):
    return render(request, 'user_center/notice.html')
