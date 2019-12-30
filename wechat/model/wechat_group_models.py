from django.db import models
from wechat.models import User

from wechat.model.article_models import Category, Type


class Profession(models.Model):
    """
         微信号行业表
    """
    nid = models.AutoField(primary_key=True)
    profession = models.CharField(verbose_name='行业', max_length=32)

    class Meta:
        db_table = 'wechat_wechat_profession'
class Topic(models.Model):
    """
         微信号标题表
    """
    nid = models.AutoField(primary_key=True)
    profession = models.CharField(verbose_name='标题', max_length=32)

    class Meta:
        db_table = 'wechat_wechat_topic'
class WechatInfo(models.Model):
    '''
    微信号基表
    '''
    profession = models.ForeignKey(Profession, null=True, validators='行业', on_delete=models.CASCADE)
    area = models.CharField(null=True, max_length=200, validators='地区')
    nik_name = models.CharField(null=True, max_length=200, validators='名称')
    tag = models.CharField(null=True, max_length=200, validators='标签')
    phone = models.CharField(null=True, max_length=200, validators='联系人电话')
    qq = models.CharField(null=True, max_length=200, validators='联系人qq号')
    avatars = models.CharField(null=True, max_length=200, validators='头像')
    qrc = models.CharField(null=True, max_length=200, validators='群二维码')
    introduce = models.CharField(null=True, max_length=10000, validators='介绍')
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

    user = models.ForeignKey(verbose_name='作者', to=User, to_field='nid', on_delete=models.CASCADE)

    class Meta:
        abstract = True


class WechatGroup(WechatInfo):
    '''
    微信群表
    '''
    nid = models.AutoField(primary_key=True)
    topic = models.ForeignKey(Topic, null=True, validators='类别（微信红包，普通）', on_delete=models.CASCADE)
    master_wechat_account = models.CharField(null=True, max_length=200, validators='群主微信号')
    link = models.CharField(null=True, max_length=200, validators='联系人')
    stataus = models.CharField(null=True, max_length=200, validators='状态')

    class Meta:
        db_table = 'wechat_wechatgroup'


class SellWechatGroup(WechatInfo):
    '''
    出售微信群表
    '''
    nid = models.AutoField(primary_key=True)
    p_count = models.CharField(null=True, max_length=200, validators='人数')
    price = models.CharField(null=True, max_length=200, validators='价格')
    master_wechat_account = models.CharField(null=True, max_length=200, validators='群主微信号')
    group_cover = models.CharField(null=True, max_length=200, validators='群封面')
    master_wechat_qrc = models.CharField(null=True, max_length=200, validators='群主微信二维码')

    class Meta:
        db_table = 'wechat_sell_wechat_group'


class SelfWechat(WechatInfo):
    '''
    个人微信号表
    '''
    nid = models.AutoField(primary_key=True)
    brithday = models.DateField(auto_now_add=True, verbose_name='生日')
    wechat = models.CharField(null=True, max_length=200, validators='卖点介绍')

    class Meta:
        db_table = 'wechat_self_wechat'


class PublicWechat(WechatInfo):
    '''
    公众号
    '''
    nid = models.AutoField(primary_key=True)
    wehcat_id = models.CharField(null=True, max_length=200, validators='公众号id')
    group_cover = models.CharField(null=True, max_length=200, validators='群封面')

    class Meta:
        db_table = 'wechat_public_wechat'
