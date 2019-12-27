from django.db import models
from wechat.models import User


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
    group_cover = models.CharField(null=True, max_length=200, validators='封面图')
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
