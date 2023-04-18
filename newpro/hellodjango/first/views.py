#coding=utf-8
from django.shortcuts import render,redirect
from django.http import JsonResponse
# Create your views here.
from random import sample
from django.http import HttpResponse,HttpRequest
from first.models import TbSubject,TbTeacher,User
from first.utils import *
from first.Captcha import Captcha
def show_index(request):
    fruits = ['Apple','Orange','Pitaya','Durian','Waxberry','Blueberry','Grape','Peach','Pear','Banana','Watermelon','Mango']
    seleted_fruits = sample(fruits,3)
    return render(request,'index.html',{'fruits':seleted_fruits})

def show_subject(request):
    subjects = TbSubject.objects.all().order_by('no')
    if request.session.get('username'):
        print(request.session.get('username'))
        username = request.session['username']
        user = User.objects.filter(username=username)
        print(type(user))
        print(user[0].username)
    # print(request.session.get['username'])
    # print(request.session['userid'])
    return render(request,'subject.html',{'subjects':subjects})

def show_teacher(request):
    try:
        sno = int(request.GET.get('sno'))
        teachers = []
        if sno:
            subject = TbSubject.objects.only('name').get(no=sno)
            teachers = TbTeacher.objects.filter(sno=subject.no).order_by('no')

        return render(request,'teacher.html',{'subject':subject,'teachers':teachers})
    except(ValueError,TbSubject.DoesNotExist):
        return redirect('/')

def praise_or_criticize(request):
    '''好评'''
    try:
        tno = int(request.GET.get('tno'))
        teacher = TbTeacher.objects.get(no=tno)
        print(teacher.gcount)
        if request.path.startswith('/praise'):
            teacher.gcount+=1
            count = teacher.gcount
            print(teacher.gcount)
        else:
            teacher.bcount+=1
            count = teacher.bcount
        teacher.save()
        data={'code':20000,'mesg':'操作成功','count':count}
    except(ValueError,TbTeacher.DoseNotExist):
        data={'code':20001,'mesg':'操作失败'}
    return JsonResponse(data)

def get_captcha(request: HttpRequest) -> HttpResponse:
    """验证码"""
    captcha_text = gen_random_code()
    request.session['captcha'] = captcha_text
    image_data = Captcha.instance().generate(captcha_text)
    return HttpResponse(image_data,content_type='image/png')

def login(request: HttpRequest) -> HttpResponse:
    hint = ''
    if request.method == 'POST':
        print('login')
        username = request.POST.get('username')
        password = request.POST.get('password')
        captcha = request.POST.get('captcha')
        print(username,captcha)
        if username and password and captcha:
            password = gen_md5_digest(password)
            user = User.objects.filter(username=username, password=password).first()
            if user:
                if request.session['captcha'] == captcha:
                    request.session['userid'] = user.no
                    request.session['username'] = user.username
                    return redirect('/')
                else:
                    hint = '验证码不正确'
            else:
                hint = '用户名或密码错误'
        else:
            hint = '请输入有效的用户名和密码'
    return render(request, 'login.html', {'hint': hint})

def logout(request):
    """注销"""
    request.session.flush()
    return redirect('/')
def register(request):
    hint =''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        captcha = request.POST.get('captcha')
        user = User.objects.filter(username=username).first()
        if request.session['captcha'] == captcha:
            if user:
                hint = '账号已经存在'
            else:
                password = gen_md5_digest(password)
                u = User(username=username,password=password)
                u.save()
                return redirect('/')
        else:
            hint = '验证码错误'
            print(request.session['captcha'],captcha)
    return render(request,'register.html',{'hint':hint})