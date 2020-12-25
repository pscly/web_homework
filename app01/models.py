from django.db import models

# Create your models here.

class Commodity(models.Model):
    title = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    img_path = models.FileField(upload_to='img/Com')
    text = models.TextField()


class User(models.Model):
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=64)

    is_root = models.BooleanField(default=0)
    is_vip = models.BooleanField(default=0)

    money = models.DecimalField(max_digits=12, decimal_places=2, default=10.00)
    user_ico = models.FileField(upload_to='user_ico/%Y/', default='user_ico/01default.jpg')  # 实际上的用户目录是MEDIA_URL + user_ico

    is_ban = models.BooleanField(default=0)

    qianming = models.CharField(max_length=64)   # 签名
    wenzhang = models.ForeignKey(to='Wenzhang')

class Files(models.Model):
    file_name = models.CharField(max_length=255)
    file_path_name = models.CharField(max_length=255)
    file_path = models.FileField(upload_to='user_file/%Y_%m/')
    file_date = models.DateTimeField(auto_now_add=True)
    is_look = models.BooleanField(default=1)

    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # 价格
    count_click = models.IntegerField(default=0)    # 点击的次数

    user = models.ForeignKey(to='User')

    is_ban = models.BooleanField(default=0)


class Fen_lei(models.Model):
    fen_lei_name = models.CharField(max_length=255)
    count_click_1 = models.IntegerField()
    bei_zhu = models.CharField(max_length=255, default='')


class Wenzhang(models.Model):
    biaoti = models.CharField(max_length=64)
    zhengwen = models.TextField()
    data = models.DateTimeField(auto_now_add=True)
    data_change = models.DateTimeField(auto_now=True)



