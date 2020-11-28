from django.test import TestCase

# Create your tests here.
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web_homework.settings")
    import django

    django.setup()

    from app01 import models

    # 一对多
    #
    # user_obj = models.User.objects.filter(username='pscly').first()
    # print(user_obj.username)    # pscly

    # models.Files.objects.create(file_name='a1', user)
    # file_obj = models.Files.objects.all()
    #
    # file_obj_count = file_obj.count()
    # file_obj_count_ye, file_obj_count_yu = (file_obj_count // 6) + 1, file_obj_count % 6
    # print(file_obj_count_ye, file_obj_count_yu)
    # file_obj_count_ye, file_obj_count_yu = divmod(file_obj_count, 6)
    # print(file_obj_count_ye, file_obj_count_yu)

    # objs = models.Files.objects.order_by('-file_date').filter(user=35)
    # for i in objs:
    #     print(i.file_name)

    # 多对多

    for i in range(5):
        username = input(":>>")
        password = '123'
        user_obj = models.User(username=username, password=password)
        user_obj.save()