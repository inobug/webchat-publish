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



class Category(models.Model):
    """
    博主个人文章分类表
    """
    nid = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name='分类标题', max_length=32)

    # 与博客建立一个一对多的关系 此表 是多

    def __str__(self):
        return self.title


class Tag(models.Model):
    # 标签信息表
    nid = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name='标签名称', max_length=32)

    # 一对多的关系 此表 是多

    def __str__(self):
        return self.title


class Article(models.Model):
    # 文章表
    nid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, verbose_name='文章标题')
    abstract = models.CharField(max_length=200, verbose_name='文章摘要')
    desc = models.CharField(max_length=10000, verbose_name='文章描述')
    group_cover = models.CharField(null=True, max_length=200, verbose_name='封面图')
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    # 内容
    content = models.TextField()
    # 点赞评论计数
    comment_count = models.IntegerField(default=0)
    up_count = models.IntegerField(default=0)
    down_count = models.IntegerField(default=0)
    # 与用户建立一对多的关系 用户是一 此表是多
    user = models.ForeignKey(verbose_name='作者', to=User, to_field='nid', on_delete=models.CASCADE)
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


class Image(models.Model):
    """
    搞笑图片
    """
    nid = models.AutoField(primary_key=True)

    title = models.CharField(max_length=50, verbose_name='图片名')
    desc = models.CharField(max_length=255, verbose_name='图片描述')
    type = models.CharField(max_length=50, verbose_name='分类')
    src = models.CharField(max_length=50, verbose_name='路径')
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    user = models.ForeignKey(verbose_name='作者', to=User, to_field='nid', on_delete=models.CASCADE)

    class Meta:
        db_table = 'wechat_image'


class Stroy(models.Model):
    """
    搞笑段子
    """
    nid = models.AutoField(primary_key=True)

    title = models.CharField(max_length=50, verbose_name='标题')
    desc = models.CharField(max_length=1000, verbose_name='内容')
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    user = models.ForeignKey(verbose_name='作者', to=User, to_field='nid', on_delete=models.CASCADE)

    class Meta:
        db_table = 'wechat_story'


class Advert(models.Model):
    """
    广告
    """
    nid = models.AutoField(primary_key=True)

    title = models.CharField(max_length=50, verbose_name='品牌标题')
    goodness = models.CharField(max_length=500, verbose_name='品牌优势')
    desc = models.CharField(max_length=500, verbose_name='品牌描述')
    qrc = models.CharField(max_length=500, verbose_name='微信号二维码')
    wechat = models.CharField(max_length=500, verbose_name='微信号')
    link = models.CharField(max_length=500, verbose_name='联系人')
    phone = models.CharField(max_length=500, verbose_name='电话')
    qq = models.CharField(max_length=500, verbose_name='qq')
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    user = models.ForeignKey(verbose_name='作者', to=User, to_field='nid', on_delete=models.CASCADE)

    class Meta:
        db_table = 'wechat_advert'









class WechatInfo(models.Model):
    '''
    微信号基表
    '''
    profession = models.CharField(null=True, max_length=200, verbose_name='行业')
    area = models.CharField(null=True, max_length=200, verbose_name='地区')
    nik_name = models.CharField(null=True, max_length=200, verbose_name='名称')
    tag = models.CharField(null=True, max_length=200, verbose_name='标签')
    phone = models.CharField(null=True, max_length=200, verbose_name='联系人电话')
    qq = models.CharField(null=True, max_length=200, verbose_name='联系人qq号')
    avatars = models.CharField(null=True, max_length=200, verbose_name='头像')
    qrc = models.CharField(null=True, max_length=200, verbose_name='群二维码')
    introduce = models.CharField(null=True, max_length=10000, verbose_name='介绍')
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

    user = models.ForeignKey(verbose_name='作者', to=User, to_field='nid', on_delete=models.CASCADE)

    class Meta:
        abstract = True


class WechatGroup(WechatInfo):
    '''
    微信群表
    '''
    nid = models.AutoField(primary_key=True)
    type = models.CharField(null=True, max_length=200, verbose_name='类别（微信红包，普通）')
    master_wechat_account = models.CharField(null=True, max_length=200, verbose_name='群主微信号')
    link = models.CharField(null=True, max_length=200, verbose_name='联系人')
    stataus = models.CharField(null=True, max_length=200, verbose_name='状态')

    class Meta:
        db_table = 'wechat_wechatgroup'


class SellWechatGroup(WechatInfo):
    '''
    出售微信群表
    '''
    nid = models.AutoField(primary_key=True)
    p_count = models.CharField(null=True, max_length=200, verbose_name='人数')
    price = models.CharField(null=True, max_length=200, verbose_name='价格')
    master_wechat_account = models.CharField(null=True, max_length=200, verbose_name='群主微信号')
    group_cover = models.CharField(null=True, max_length=200, verbose_name='群封面')
    master_wechat_qrc = models.CharField(null=True, max_length=200, verbose_name='群主微信二维码')

    class Meta:
        db_table = 'wechat_sellwechatgroup'


class SelfWechat(WechatInfo):
    '''
    个人微信号表
    '''
    nid = models.AutoField(primary_key=True)
    brithday = models.DateField(auto_now_add=True, verbose_name='生日')
    wechat = models.CharField(null=True, max_length=200, verbose_name='卖点介绍')

    class Meta:
        db_table = 'wechat_selfwechat'


class PublicWechat(WechatInfo):
    '''
    公众号
    '''
    nid = models.AutoField(primary_key=True)
    wehcat_id = models.CharField(null=True, max_length=200, verbose_name='公众号id')
    group_cover = models.CharField(null=True, max_length=200, verbose_name='群封面')

    class Meta:
        db_table = 'wechat_publicwechat'



#
# class Module(models.Model):
#     """
#     模块
#     """
#     nid = models.AutoField(primary_key=True)
#     module_name = models.CharField(null=True, verbose_name='模块名', max_length=200)
#     moule_detail = models.CharField(null=True, verbose_name='模块信息', max_length=200)
#
#
# class WechatType(models.Model):
#     """
#     微信类别
#     """
#     nid = models.AutoField(primary_key=True)
#     wechat_title = models.CharField(null=True, verbose_name='微信号类别', max_length=200)
#     module = models.ForeignKey(Module, null=True, verbose_name='模块', on_delete=models.CASCADE)
#
#
# class WechatDetail(models.Model):
#     """
#     微信详情
#     """
#     nid = models.AutoField(primary_key=True)
#     publish_time = models.DateField(null=True, verbose_name='发布时间')
#     area = models.CharField(null=True, verbose_name='地区', max_length=200)
#     attention = models.IntegerField(null=True, verbose_name='关注度')
#     assess = models.IntegerField(null=True, verbose_name='评价度')
#     type = models.ForeignKey(WechatType, verbose_name='类别', on_delete=models.CASCADE)
#     detail = models.CharField(null=True, verbose_name='详情介绍', max_length=1000)
#     head_img = models.CharField(null=True, verbose_name='头像（路径）', max_length=1000)
#     ocr_img = models.CharField(null=True, verbose_name='二维码（路径）', max_length=1000)
#     is_pay = models.CharField(null=True, verbose_name='是否缴费(1,0)', max_length=200)
#     pay_level = models.CharField(null=True, verbose_name='缴费级别', max_length=200)
#     user = models.ForeignKey(to='User',to_field='nid', verbose_name='发布人',on_delete=models.CASCADE )
#
#
# class Tip(models.Model):
#     """
#     微信标签
#     """
#     nid = models.AutoField(primary_key=True)
#     tip_name = models.CharField(null=True, verbose_name='标签名', max_length=200)
#     wechat = models.ManyToManyField(WechatDetail)
#
#
# class Blog(models.Model):
#     """
#     博客信息
#     """
#     nid = models.AutoField(primary_key=True)
#     title = models.CharField(verbose_name='个人博客标题', max_length=64)
#     site_name = models.CharField(verbose_name='站点名称', max_length=64)
#     theme = models.CharField(verbose_name='博客主题', max_length=32)
#
#     def __str__(self):
#         return self.title
#
#
# class Category(models.Model):
#     """
#     博主个人文章分类表
#     """
#     nid = models.AutoField(primary_key=True)
#     title = models.CharField(verbose_name='分类标题', max_length=32)
#     # 与博客建立一个一对多的关系 此表 是多
#     blog = models.ForeignKey(verbose_name='所属博客', to='Blog', to_field='nid', on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.title
#
# class Tag(models.Model):
#     # 标签信息表
#     nid = models.AutoField(primary_key=True)
#     title = models.CharField(verbose_name='标签名称', max_length=32)
#     # 一对多的关系 此表 是多
#     blog = models.ForeignKey(verbose_name='所属博客', to='Blog', to_field='nid', on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.title
# class Article(models.Model):
#     # 文章表
#     nid = models.AutoField(primary_key=True)
#     title = models.CharField(max_length=50, verbose_name='文章标题')
#     desc = models.CharField(max_length=255, verbose_name='文章描述')
#     create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
#     # 内容
#     content = models.TextField()
#     # 点赞评论计数
#     comment_count = models.IntegerField(default=0)
#     up_count = models.IntegerField(default=0)
#     down_count = models.IntegerField(default=0)
#     # 与用户建立一对多的关系 用户是一 此表是多
#     user = models.ForeignKey(verbose_name='作者', to='User', to_field='nid', on_delete=models.CASCADE)
#     # 与分类是一对多的关系 分类表示一  此表是多
#     category = models.ForeignKey(to='Category', to_field='nid', null=True, on_delete=models.CASCADE)
#     # 与标签表示多对多的关系 此处用through 是不让系统自动建立默认的关系表,从而使用我们自己创建的关系表 方便以后扩展
#     tags = models.ManyToManyField(
#         to="Tag",
#         through='Article2Tag',
#     )
#
#     def __str__(self):
#         return self.title
#
#     # 文章表与 标签表的关系表 (自己创建)
#
#
# class Article2Tag(models.Model):
#     nid = models.AutoField(primary_key=True)
#     article = models.ForeignKey(verbose_name='文章', to="Article", to_field='nid', on_delete=models.CASCADE)
#     tag = models.ForeignKey(verbose_name='标签', to="Tag", to_field='nid', on_delete=models.CASCADE)
#
#     class Meta:
#         unique_together = [
#             ('article', 'tag'),
#         ]
#
#     def __str__(self):
#         v = self.article.title + "---" + self.tag.title
#         return v

