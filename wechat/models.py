from django.db import models


# Create your models here.
class User(models.Model):
    user_id = models.CharField(unique=True, primary_key=True, max_length=200)
    user_name = models.CharField(null=True, verbose_name='用户名', max_length=200)
    password = models.CharField(null=True, verbose_name='密码', max_length=200)
    pet_name=models.CharField(null=True, verbose_name='昵称', max_length=200)

class Module(models.Model):
    module_id = models.CharField(unique=True, primary_key=True, max_length=200)
    module_name = models.CharField(null=True, verbose_name='模块名', max_length=200)
    moule_detail = models.CharField(null=True, verbose_name='模块信息', max_length=200)


class WechatType(models.Model):
    wechat_type_id = models.CharField(unique=True, primary_key=True, max_length=200)
    wechat_title = models.CharField(null=True, verbose_name='微信号标题', max_length=200)
    module = models.ForeignKey(Module, null=True, verbose_name='模块', on_delete=models.CASCADE)


class WechatDetail(models.Model):
    wechat_id = models.CharField(unique=True, primary_key=True, max_length=200)
    publish_time = models.DateField(null=True, verbose_name='发布时间')
    area = models.CharField(null=True, verbose_name='地区', max_length=200)
    attention = models.IntegerField(null=True, verbose_name='关注度')
    assess = models.IntegerField(null=True, verbose_name='评价度')
    type = models.ForeignKey(WechatType, verbose_name='类别', on_delete=models.CASCADE)
    detail = models.CharField(null=True, verbose_name='详情介绍', max_length=1000)
    head_img = models.CharField(null=True, verbose_name='头像（路径）', max_length=1000)
    ocr_img = models.CharField(null=True, verbose_name='二维码（路径）', max_length=1000)
    is_pay = models.CharField(null=True, verbose_name='是否缴费(1,0)', max_length=200)
    pay_level = models.CharField(null=True, verbose_name='缴费级别', max_length=200)


class Tip(models.Model):
    tip_id = models.CharField(unique=True, primary_key=True, max_length=200)
    tip_name = models.CharField(null=True, verbose_name='标签名', max_length=200)
    wechat = models.ManyToManyField(WechatDetail)
