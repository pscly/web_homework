from django.shortcuts import render, HttpResponse, redirect
# from cly_1.ip import *
from app01.cly_1.fenyeqi import *
from app01.cly_1 import funcs_1
from app01 import models
from django.core.files import File
import json
from functools import wraps
from app01 import my_funcs
from app01.yanzhengma import *  # 验证码


def login_auth(func):
    @wraps(func)
    def inner(request, *args, **kwargs):
        if request.session.get('username'):
            res = func(request, *args, **kwargs)
            return res

        urls = request.get_full_path()  # /home/
        return redirect('/login?to_url=%s' % urls)

    return inner


def quanxian_auth(request, user_obj, d1, to_quanxian=2):
    '''
    登录的权限判断， 传入数字进行判断(数据库保存的用户类型是数字)
    :param request:  用来返回网页
    :param user_obj: 用来查看用户的类型
    :param d1: 发送到前端
    :param to_quanxian: 用户的类型，输入数字就好了， 自动列表生成式
    :return:
    '''
    l1 = [_ for _ in range(1,to_quanxian+1)]

    if user_obj.user_type not in l1:
        print(user_obj.user_type)
        d1['error_msg'] = '权限不足'
        return False
    return True

def index(request):
    print('用户的ip', funcs_1.get_ip(request))
    now_page = '登录'
    now_tou = 't_index'
    ip_addr = funcs_1.get_ip(request)
    username = request.session.get('username')

    if username:
        user_obj = models.User.objects.filter(username=username).first()

    if request.method == 'GET':
        # 不出意外的话这里要写搜索，（优先度5(最低)）

        return render(request, 'index.html', locals())

    if request.method == 'POST':
        return HttpResponse('<h1 >这个功能还没做,</h1>')


def login(request):
    now_page = '登录'
    now_tou = 't_login'
    reg = False

    if request.method == 'GET':
        return render(request, 'login_he.html', locals())

    # if request.GET:
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        password = funcs_1.get_pwd_hash(password)

        user_obj = models.User.objects.filter(username=username).first()
        if not user_obj:
            error_msg = '没有这个用户'
            return render(request, 'error.html', {'error_msg': error_msg})

        if not user_obj.password == password:
            error_msg = '密码错误了'
            return render(request, 'error.html', {'error_msg': error_msg})

        ret_obj1 = redirect('/index/')

        to_url = request.GET.get('to_url')
        if to_url:
            ret_obj1 = redirect(to_url)

        request.session['username'] = username
        return ret_obj1


def reg(request):
    now_page = '注册'
    now_tou = 't_reg'
    d1 = my_funcs.get_tou(request, now_tou)
    d1['now_page'] = now_page

    if request.is_ajax():
        if request.method == 'POST':
            def_type = request.POST.get('def_type')
            send_data = {'stus': 201, 'data': None}
            if def_type == '1':
                '''
                    这里是注册时的用户输入框
                '''
                username = request.POST.get('username')
                send_data = {'stus': 200, 'data': '可以使用'}
                if len(username) < 2:
                    send_data = {'stus': 201, 'data': '你这名字也太短了吧'}
                if len(username) > 8:
                    send_data = {'stus': 200, 'data': '……我感觉你这名字有点长，不过算了，你随意'}
                if ' ' in username:
                    send_data = {'stus': 201, 'data': '用户名请不要用空格'}

                if models.User.objects.filter(username=username).first():
                    send_data = {'stus': 201, 'data': '有这人了'}

                send_data = json.dumps(send_data)
                return HttpResponse(send_data)

            if def_type == '2':
                '''
                    这个是发送手机的验证码
                '''
                phone_num = request.POST.get('phone_num')
                yzm_num, _ = get_yanzhengma()  # 生成随机的4位纯数字验证码

                send_txy_yzm(yzm_num, phone_num)      # 通过腾讯云发送验证码
                send_data = {'stus': 200, 'yzm_num': yzm_num}
                print('手机验证码是', yzm_num)

                send_data = json.dumps(send_data)
                return HttpResponse(send_data)

            if def_type == '3':
                '''
                    这个是刷新用户注册时的图片验证1码
                '''
                yzm_str, yzm_img = get_yanzhengma()
                yzm_img = get_pil_base64(yzm_img)  # 将图片转为二进制
                yzm_img = yzm_img.decode()

                send_data = {'stus': 200, 'yzm_img_2': yzm_img, 'yzm_img_str': yzm_str}

                send_data = json.dumps(send_data)
                return HttpResponse(send_data)

    if request.method == 'GET':
        yzm_str, yzm_img = get_yanzhengma()
        d1['yzm_str'] = yzm_str
        d1['yzm_img'] = yzm_img
        d1['yzm_img_2'] = get_pil_base64(yzm_img)
        return render(request, 'login_he.html', d1)

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        print(password, '++++', password2)
        # hash密码在后面
        user_ico = request.POST.get('user_ico')
        user_type = request.POST.get('user_type')
        user_phone = request.POST.get('phone')

        files = request.FILES
        print('views-->reg')  # TODO
        if not username:
            return render(request, 'error.html', {'error_msg': '用户名长度太短了'})
        if len(username) < 3:
            return render(request, 'error.html', {'error_msg': '用户名长度太短了'})
        if ' ' in username:
            return render(request, 'error.html', {'error_msg': '用户名不能有空格'})
        if len(password) < 3:
            return render(request, 'error.html', {'error_msg': '密码长度太短了'})
        if password != password2:
            return render(request, 'error.html', {'error_msg': '两次的密码不同啊'})
        # # # #  我应该在这里吧密码hash一下
        password = funcs_1.get_pwd_hash(password)
        print(username)
        user_obj = models.User.objects.filter(username=username)

        if user_obj:
            return redirect('/reg')

        # if not user_type.isdecimal():
        #     return redirect('/reg')
        #
        # user_type = int(user_type)

        if files:
            django_file = File(files.get('user_ico'))  # 先读取文件， 然后将其转换为orm可识别的对象
            # # 保存的文件名就会是 用户名+_X_+文件名
            django_file.name = username + '_X_' + django_file.name

            user_obj = models.User(username=username, password=password, user_ico=django_file)
        else:
            # 如果用户不上传头像，那就直接使用默认的头像
            user_obj = models.User(username=username, password=password)

        user_obj.save()

        ret_obj1 = redirect('/index/')
        request.session['username'] = username
        return ret_obj1


@login_auth
def logout(request):
    request.session.flush()
    return redirect('/index/')


@login_auth
def home(request):
    if request.session.get('username'):
        s1 = request.session.get('username')
        return HttpResponse(f'你已经登录了{s1}')
    return HttpResponse('你没有登陆')





@login_auth
def file_share(request):
    now_tou = 't_file_share'
    d1 = my_funcs.get_tou(request, now_tou)

    all_user_objs = models.User.objects.filter(is_ban=0)
    d1['all_user_objs'] = all_user_objs

    if request.method == 'GET':
        file_objs = models.Files.objects.filter(is_look=1).order_by('-file_date')

        file_objs = my_funcs.set_count_num(file_objs)

        now_page_num = request.GET.get('page', 1)

        page_obj = Pagination(now_page_num, file_objs.count(), 6, 7)
        page_datas = file_objs[page_obj.start:page_obj.end]

        d1['page_obj'] = page_obj
        d1['page_datas'] = page_datas

        return render(request, 'file_share.html', d1)

    if request.method == 'POST':
        file = request.FILES.get('user_up_file')
        if file:
            django_file = File(file)
            file_name = django_file.name
            django_file.name = d1['username'] + '_X_' + django_file.name  # 文件名字我想保存为  用户名+_X_+文件名
            # 这里理解起来可能有些绕， file_name 是文件本身的名字， file_path_name 是文件的保存名字  就是加了上面的东西
            up_file_obj = models.Files(file_name=file_name, file_path_name=django_file.name, file_path=django_file,
                                       user=d1['user_obj'])
            up_file_obj.save()
        return redirect('/file_share')




















@login_auth
def project_guanli(request):
    now_tou = 'project_guanli'
    d1 = my_funcs.get_tou(request, now_tou)
    user_obj = d1.get('user_obj')
    if not quanxian_auth(request, user_obj, d1, 2):
        return render(request, 'error.html', d1)

    project_objs = models.Projects.objects.filter(is_disabled=0).all()
    project_objs = my_funcs.set_count_num(project_objs)
    d1['project_objs'] = project_objs
    return render(request, 'projects/projects_guanli.html', d1)


@login_auth
def project_add(request):
    now_tou = 'project_add'
    d1 = my_funcs.get_tou(request, now_tou)
    user_obj = d1.get('user_obj')

    if request.method == 'GET':
        if not quanxian_auth(request, user_obj, d1, 2):
            return render(request, 'error.html', d1)

        return render(request, 'projects/project_add.html', d1)

    if request.method == 'POST':
        project_name = request.POST.get('project_name')
        project_obj = models.Projects(project_name=project_name)
        project_obj.save()
        return redirect('/project_gl')


@login_auth
def user_guanli(request):
    d1 = my_funcs.get_tou(request, '用户管理')

    return render(request, 'templates/uesrs/user_guanli.html', d1)


def user_home(request, to_username=None):
    # # TODO 这里写个用户的主页系统， 别人可以访问到的那种
    d1 = my_funcs.get_tou(request, '个人主页')
    print('none')
    if not to_username:
        if not d1.get('username'):
            return redirect('/index')
    d1['to_username'] = to_username
    if to_username == request.session.get('username'):
        # 如果是本人访问自己的主页 TODO 懂得都懂，/滑稽
        pass

    return render(request, 'templates/uesrs/user_home.html', d1)


@login_auth
def project_user_edit(request, to_project=None):
    now_tou = '编辑项目相关人员'
    d1 = my_funcs.get_tou(request, now_tou)
    user_obj = d1.get('user_obj')


    if request.method == 'GET':
        if not quanxian_auth(request, user_obj, d1, 2):
            return render(request, 'error.html', d1)

        user_objs = models.User.objects.filter(is_disabled=0, projects=to_project).all()    # 拿到所有在这个项目中的用户
        project_obj = models.Projects.objects.filter(id=to_project).first()
        # if user_obj.user_type == 1:
        for i in user_objs:
            i.user_type_name = i.get_user_type_display()
        d1['user_objs'] = user_objs
        d1['project_obj'] = project_obj
        return render(request, 'projects/project_user_guanli.html', d1)

    return HttpResponse('project_user_edit %s' % to_project)


@login_auth
def project_edit(request, to_project=None):
    # TODO 2
    now_tou = '编辑项目'
    d1 = my_funcs.get_tou(request, now_tou)
    user_obj = d1.get('user_obj')

    if not quanxian_auth(request, user_obj, d1, 2):
        return render(request, 'error.html', d1)

    return HttpResponse('project_edit %s' % to_project)


@login_auth
def qndxx(request):
    # return render(request, 'qndxx.html')
    qi = 10
    pian = 5
    return redirect(f'http://dxx.wwwtop.top/dxx_video?a={qi}&b={pian}&c=1&d=1&z=200s')
