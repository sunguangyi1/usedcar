from django.db import models

# Create your models here.
from sale.models import Carinfo
from userinfo.models import Userinfo

STATUS = (
    (0,'已出价'),
    (1,'已支付'),
    (2,'交易成功'),
    (3,'订单关闭'),
    (4,'交易中'),
)

class Cartinfo(models.Model):
    price = models.DecimalField('价格',max_digits=7,decimal_places=2)
    car_id = models.ForeignKey(Carinfo)
    user_id = models.ForeignKey(Userinfo)

    def __str__(self):
        return '{0}-{1}'.format(self.user_id.username,self.car_id.name)

    class Meta:
        db_table = 'Cart'
        verbose_name = '意向表'
        verbose_name_plural = verbose_name

class Orderinfo(models.Model):
    name = models.CharField('车辆信息',max_length=150,null=False)
    price = models.DecimalField('价格',max_digits=7,decimal_places=2)
    num = models.CharField('订单号',max_length=20,null=False)
    status = models.IntegerField('订单状态',choices=STATUS,default=0)
    isDelete = models.BooleanField('是否删除',default=False)
    sell_id = models.ForeignKey(Userinfo,related_name='selluser')
    buy_id = models.ForeignKey(Userinfo,related_name='buyuser')

    def __str__(self):
        return self.num

    class Meta:
        db_table = 'Order'
        verbose_name = '订单'
        verbose_name_plural = verbose_name