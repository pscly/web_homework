from django.db import models


# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    number_1 = models.IntegerField()    # 用户的工号

    choices = [
        (1, '最高管理员'),
        (2, '项目经理'),
        (3, '标注员'),
        (4, '质检员'),
    ]
    user_type = models.IntegerField(choices=choices, default=4)    # 用户的类型
    # my_project = models.ManyToManyField(to='Projects')  # 对应的项目信息(多对多)

    user_ico = models.FileField(upload_to='user_ico/%Y/',default='user_ico/01default.jpg')  # 实际上的用户目录是MEDIA_URL + user_ico

    is_disabled = models.BooleanField(default=0)  # 是否将用户禁用
    is_who = models


class Projects(models.Model):
    project_name = models.CharField(max_length=64)
    project_text = models.TextField(null=True)  # 项目的详细信息
    project_jindu = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)  # 项目的总体进度
    # project_jindu = models.IntegerField(default=0)  # 项目的总体进度
    is_over = models.BooleanField(default=0)  # 项目是否完成
    to_user = models.ManyToManyField(to='User', null=True)  # 这个项目对应的用户
    is_disabled = models.BooleanField(default=0)  # 是否禁用(删除)项目


class Today_work(models.Model):
    project_name = models.OneToOneField(to='Projects')    # 什么项目
    user = models.OneToOneField(to='User')  # 谁
    project_jindu = models.DecimalField(max_digits=6, decimal_places=4)  # 今天的项目进度
    now_day = models.DateField(auto_now_add=True)   # 今天是哪天


