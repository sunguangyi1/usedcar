from django.db import models
from django.contrib.auth.models import AbstractUser
SEX_CHOICES = (
    (1,'男'),
    (0,'女'),
)
BANK = (
    (0,'冻结'),
    (1,'未审核'),
    (2,'已审核'),
    (3,'已删除'),
)

# Create your models here.
class Userinfo(AbstractUser):
    uphone = models.CharField('手机号',max_length=20,null=True,blank=True,unique=True)
    realname = models.CharField('真实姓名',max_length=20,null=True,blank=True)
    uindetity = models.CharField('身份证',max_length=30,null=True,blank=True)
    sex = models.IntegerField('性别',choices=SEX_CHOICES,default=1)
    address = models.CharField('地址',max_length=50,null=True,blank=True)

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'Users'
        verbose_name = '用户信息表'
        verbose_name_plural = verbose_name



class Messageinfo(models.Model):
    mes = models.CharField('消息',max_length=100,null=True)
    date = models.DateTimeField('日期',auto_now=True)
    user_id = models.ForeignKey(Userinfo)

    def __str__(self):
        return self.user_id.username

    class Meta:
        db_table = 'Message'
        verbose_name = '消息'
        verbose_name_plural = verbose_name

class Bankinfo(models.Model):
    bank = models.CharField('开户银行',max_length=20,null=False)
    num = models.CharField('卡号',max_length=30,null=False)
    status = models.IntegerField('银行卡状态',choices=BANK,default=0)
    user_id = models.ForeignKey(Userinfo)

    def __str__(self):
        return self.user_id.username

    class Meta:
        db_table = 'Bank'
        verbose_name = '银行信息'
        verbose_name_plural = verbose_name