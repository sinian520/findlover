from django.shortcuts import render
from .models import user,matchmaker,memberprice,partyapply,partymessage,xinwen,text,friends,userdynamic,comment,UserToken,EmailVerify
from django.views.decorators.http import require_http_methods
#序列化工具将Django的模型‘翻译’成其它格式的数据,用于数据交换\传输过程。
from django.core import serializers
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from . import models
import time
import random
#引入使token加密
from django.core import signing
#邮箱验证码
from emailtool.send_mail import send_email_code


# Create your views here.
# 用户登录
@csrf_exempt
def LoginView(request):
    ret = {'code': 1000, 'msg': None}
    username = request.POST.get('username')
    pwd = request.POST.get('password')
    obj = models.user.objects.filter(emile=username, password=pwd).first()
    if not models.user.objects.filter(emile=username, password=pwd):
        ret['code']=1001
        ret['msg']='用户名或密码错误'
    # 为登录用户创建token
    token = signing.dumps(username)
    # 存在则更新，反之创建
    models.UserToken.objects.update_or_create(user=obj, defaults={'token': token})
    ret['token'] = token 
    return JsonResponse(ret)



# 用户注册邮箱验证码
@csrf_exempt
def RegisterCheck(request):
    ret = {'code': 1000, 'msg': None}
    email = request.POST.get('email')
    print(email)
    if models.user.objects.filter(emile=email):
        ret['code']=1001
        ret['msg']='该邮箱已被注册'
    else:
        newcode=send_email_code(email,1)
        ret['code']=1000
        ret['msg']='已发送验证消息到您的邮箱中'
    return JsonResponse(ret)

# 用户注册
@csrf_exempt
def Register(request):
    ret = {'code': 1000, 'msg': None}
    try:
        email = request.POST.get('email')
        print(email)
        username = request.POST.get('username')
        phone = request.POST.get('phone')
        sex = request.POST.get('sex')
        password = request.POST.get('password')
        info=request.POST.get('info')
        date=request.POST.get('date')
        where=request.POST.get('where')
        marrytype=request.POST.get('marrytype')


        t=models.user.objects.get(id=1)
        print(t.name)
        print(email)
        newuser=models.EmailVerify.objects.get(email=email)
        print(newuser)
        # 验证码一致
        if newuser.code==info:

            # 将用户信息存入数据库
            a=user()
            a.emile=email
            a.name=username
            a.sex=sex
            a.tele=phone
            a.type='普通用户'
            a.password=password
            a.status=0
            a.marriage=marrytype
            a.birthday=date
            a.live=where
            a.save()
        else:
            ret['code']=1001
            ret['msg']='验证信息错误'
    except IOError:
        ret['code']=1002
        ret['msg']='获取前端数据失败或数据库错误'
    return JsonResponse(ret)

