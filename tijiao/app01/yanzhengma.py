# coding: utf-8
# 作者:Pscly
# 创建日期: 
# 用意：
from captcha.image import ImageCaptcha
from app01.tenxun import *
import random,string

import base64
from io import BytesIO

def get_pil_base64(image):
    '''
    将PIL的图片转换为二进制的数据
    :param image:
    :return:
    '''
    img_buffer = BytesIO()
    image.save(img_buffer, format='JPEG')
    byte_data = img_buffer.getvalue()
    base64_str = base64.b64encode(byte_data)
    return base64_str




def get_yanzhengma(length=4):
    # chr_all = string.ascii_letters + string.digits
    chr_int = string.digits
    # string.ascii_letters 是大小写的所有字符串，
    # string.digits 是0-9

    chr_ = ''.join(random.sample(chr_int, length))  # 验证码的随机字符串
    image = ImageCaptcha().generate_image(chr_)
    return (chr_, image)  # 发送验证码的字符串和验证码的图片(PIL.Image.Image)


def send_yzm(yzm, phone_num):
    send_txy_yzm(yzm, phone_num)
    return None

if __name__ == '__main__':

    yzm_str, yzm_img = get_yanzhengma(6)    # 6 是长度
    print(yzm_str)


