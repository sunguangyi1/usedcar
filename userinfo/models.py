from django.db import models
from django.contrib.auth.models import AbstractUser
SEX_CHOICES = (
    (1,'男'),
    (0,'女'),
)
# Create your models here.
class Userinfo(AbstractUser):
    uphone = models.CharField('手机号',max_length=20,null=True,blank=True,unique=True)
    # uemail = models.EmailField('邮箱')
    realname = models.CharField('真实姓名',max_length=20,null=True,blank=True)
    uindetity = models.CharField('身份证',max_length=30,null=True,blank=True)
    sex = models.IntegerField('性别',choices=SEX_CHOICES,default=1)
    address = models.CharField('地址',max_length=50,null=True,blank=True)
    # isActive = models.BooleanField('是否激活',default=False)
    # isBan = models.BooleanField('是否禁用',default=False)

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'Users'
        verbose_name = '用户信息表'
        verbose_name_plural = verbose_name


# class Cartinfo(models.Model):
#     price = models.CharField('价格',max_length=20)
#     car_id = models.OneToOneField('车辆',Carinfo)
#     user_id = models.ForeignKey('用户信息',Userinfo)
#
# class Orderinfo(models.Model):
#     num = models.CharField('订单号',max_length=20)
#     status = models.CharField('订单状态',max_length=20)
#     isDelete = models.BooleanField('是否删除',default=False)
#     car_id = models.ForeignKey('车辆',Cartinfo)
#     sell_id = models.ForeignKey('卖家信息',Userinfo)
#     buy_id = models.ForeignKey('买家信息',Userinfo)
#
#
# class Messageinfo(models.Model):
#     mes = models.CharField('消息',max_length=60)
#     date = models.CharField('日期',max_length=40)
#     user_id = models.ForeignKey('用户信息',Userinfo)
#
# class Bankinfo(models.Model):
#     bank = models.CharField('开户银行',max_length=20)
#     num = models.CharField('卡号',max_length=20)
#     zhuangtai = models.CharField('状态',max_length=20)
#     user_id = models.ForeignKey('用户信息',Userinfo)