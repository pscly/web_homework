# coding: utf-8
# 作者:Pscly
# 创建日期: 
# 用意：
import hashlib


def get_pwd_hash(pwd):
    '''

    :param pwd: 传入一个字符串
    :return: 返回哈希后的字符串
    '''
    s1 = hashlib.md5()
    s1.update('pscly_666'.encode('utf-8'))
    s1.update(pwd.encode('utf-8'))

    s1_hash = s1.hexdigest()
    return s1_hash


def get_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]  # 所以这里是真实的ip
    else:
        ip = request.META.get('REMOTE_ADDR')  # 这里获得代理ip
    return ip



if __name__ == '__main__':
    s1 = input('请输入加密的字符串>>')
    print(get_pwd_hash(s1))
