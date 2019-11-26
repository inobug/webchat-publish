from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    """
    用户
    """
    nid = models.AutoField(primary_key=True)
    # user_name = models.CharField(null=True, verbose_name='用户名', max_length=200)
    # password = models.CharField(null=True, verbose_name='密码', max_length=200)
    pet_name = models.CharField(null=True, verbose_name='昵称', max_length=200)
    phone = models.CharField(null=True, verbose_name='手机号', max_length=200)
    email = models.CharField(null=True, verbose_name='邮箱', max_length=200)
    avatar = models.FileField(upload_to='avatars/', default="avatars/default.png")
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    experience=models.IntegerField(default=0)
    level=models.IntegerField(default=0)
    gold=models.IntegerField(default=20)
    area= models.CharField(null=True, verbose_name='地区', max_length=200)

    def __str__(self):
        return self.username


class Module(models.Model):
    """
    模块
    """
    nid = models.AutoField(primary_key=True)
    module_name = models.CharField(null=True, verbose_name='模块名', max_length=200)
    moule_detail = models.CharField(null=True, verbose_name='模块信息', max_length=200)


class WechatType(models.Model):
    """
    微信类别
    """
    nid = models.AutoField(primary_key=True)
    wechat_title = models.CharField(null=True, verbose_name='微信号类别', max_length=200)
    module = models.ForeignKey(Module, null=True, verbose_name='模块', on_delete=models.CASCADE)


class WechatDetail(models.Model):
    """
    微信详情
    """
    nid = models.AutoField(primary_key=True)
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
    user = models.ForeignKey(to='User',to_field='nid', verbose_name='发布人',on_delete=models.CASCADE )


class Tip(models.Model):
    """
    微信标签
    """
    nid = models.AutoField(primary_key=True)
    tip_name = models.CharField(null=True, verbose_name='标签名', max_length=200)
    wechat = models.ManyToManyField(WechatDetail)


class Blog(models.Model):
    """
    博客信息
    """
    nid = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name='个人博客标题', max_length=64)
    site_name = models.CharField(verbose_name='站点名称', max_length=64)
    theme = models.CharField(verbose_name='博客主题', max_length=32)

    def __str__(self):
        return self.title


class Category(models.Model):
    """
    博主个人文章分类表
    """
    nid = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name='分类标题', max_length=32)
    # 与博客建立一个一对多的关系 此表 是多
    blog = models.ForeignKey(verbose_name='所属博客', to='Blog', to_field='nid', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Tag(models.Model):
    # 标签信息表
    nid = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name='标签名称', max_length=32)
    # 一对多的关系 此表 是多
    blog = models.ForeignKey(verbose_name='所属博客', to='Blog', to_field='nid', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
class Article(models.Model):
    # 文章表
    nid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, verbose_name='文章标题')
    desc = models.CharField(max_length=255, verbose_name='文章描述')
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    # 内容
    content = models.TextField()
    # 点赞评论计数
    comment_count = models.IntegerField(default=0)
    up_count = models.IntegerField(default=0)
    down_count = models.IntegerField(default=0)
    # 与用户建立一对多的关系 用户是一 此表是多
    user = models.ForeignKey(verbose_name='作者', to='User', to_field='nid', on_delete=models.CASCADE)
    # 与分类是一对多的关系 分类表示一  此表是多
    category = models.ForeignKey(to='Category', to_field='nid', null=True, on_delete=models.CASCADE)
    # 与标签表示多对多的关系 此处用through 是不让系统自动建立默认的关系表,从而使用我们自己创建的关系表 方便以后扩展
    tags = models.ManyToManyField(
        to="Tag",
        through='Article2Tag',
    )

    def __str__(self):
        return self.title

    # 文章表与 标签表的关系表 (自己创建)


class Article2Tag(models.Model):
    nid = models.AutoField(primary_key=True)
    article = models.ForeignKey(verbose_name='文章', to="Article", to_field='nid', on_delete=models.CASCADE)
    tag = models.ForeignKey(verbose_name='标签', to="Tag", to_field='nid', on_delete=models.CASCADE)

    class Meta:
        unique_together = [
            ('article', 'tag'),
        ]

    def __str__(self):
        v = self.article.title + "---" + self.tag.title
        return v

