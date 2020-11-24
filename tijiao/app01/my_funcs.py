# coding: utf-8
# 作者:Pscly
# 创建日期: 
# 用意：

from app01.cly_1 import funcs_1
from app01 import models


# now_tou = 't_file_share'
# username = request.session.get('username')
# ip_addr = get_ip(request)
# user_obj = models.User.objects.filter(username=username).first()

def get_tou(request, now_tou):
    '''
    # 注意， 如果没登陆就用这个功能， user_obj 是个None， bool的None
    :param request:  这个是拿到django 的request
        1: 拿到用户的cookie
        2: 拿到用户的ip地址然后返回
    :param now_tou:  这个是拿到当前页面位置，用于前端的标记(哪一页亮)
    :return:  now_tou, username, user_obj, ip_addr
    '''
    now_tou = now_tou
    ip_addr = funcs_1.get_ip(request)
    username = request.session.get('username')
    if username:
        user_obj = models.User.objects.filter(username=username).first()
        user_type = user_obj.get_user_type_display()
        user_type_num = user_obj.user_type
        return {
            'now_tou': now_tou,
            'username': username,
            'user_obj': user_obj,
            'ip_addr': ip_addr,
            'user_type': user_type,
            'user_type_num': user_type_num,
        }

    return {
        'now_tou': now_tou,
        'username': username,
        'ip_addr': ip_addr,
        'user_obj': None,
    }


def set_count_num(objs):
    '''
    将对象按照实际的数量，重新搞一次计数
    :param objs:  传入我想要计数量的对象们(可以for循环)
    :return: 返回处理后的对象们
    '''
    try:
        my_count_num = 0
        for i in objs:
            my_count_num += 1
            i.my_count_num = my_count_num
        return objs
    except Exception as e:
        print('出现问题了， 你传了个啥噢 %s' % e)
        return objs
