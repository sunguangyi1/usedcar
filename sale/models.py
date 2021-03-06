from django.db import models

# Create your models here.
from userinfo.models import Userinfo

SHENHE =(
    (0,'审核未通过'),
    (1,'审核中'),
    (2,'审核通过'),
)

class Typeinfo(models.Model):
    name = models.CharField('品牌名',max_length=20)
    logo = models.ImageField('logo',upload_to='static/images/logo')
    isDelete = models.BooleanField('是否删除',default=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Type'
        verbose_name = '品牌表'
        verbose_name_plural = verbose_name

class Carinfo(models.Model):
    name = models.CharField('安静的就看到',max_length=30,null=False)
    date = models.IntegerField('大声',null=False)
    fadongnum = models.CharField('发动机号',max_length=20)
    mile = models.DecimalField('公里数',max_digits=7,decimal_places=2)
    isweixiu = models.BooleanField('是否维修',default=False)
    price = models.DecimalField('期望售价',max_digits=7,decimal_places=2)
    address = models.CharField('买车地址',max_length=50)
    isZhaiwu = models.BooleanField('是否有债务',default=False)
    img = models.ImageField('车辆图片',upload_to='static/upload/car',default='')
    promise = models.TextField('卖家承诺',null=True)
    shenhe = models.IntegerField('审核状态',choices=SHENHE,default=0)
    isBuy = models.BooleanField('是否购买',default=False)
    isDelete = models.BooleanField('是否删除', default=False)
    type_id = models.ForeignKey(Typeinfo)
    user_id = models.ForeignKey(Userinfo)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Car'
        verbose_name = '车辆信息表'
        verbose_name_plural = verbose_name