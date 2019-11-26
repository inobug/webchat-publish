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