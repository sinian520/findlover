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
# 取消当前函数防跨站请求伪造功能
@csrf_exempt
def LoginView(request):
    ret = {'code': 1000, 'msg': None}
    username = request.POST.get('username')
    pwd = request.POST.get('password')
    obj = models.user.objects.filter(emile=username, password=pwd).first()
    if not models.user.objects.filter(emile=username, password=pwd):
        ret['code']=1001
        ret['msg']='用户名或密码错误'
    if(obj):
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

# 显示个人信息
@csrf_exempt
def Personal(request):
    ret = {'code': 1000, 'msg': None,}
    try:
        email = request.POST.get('user')
        print(email)
        user=models.user.objects.get(emile=email)


        ret['name']=user.name
        ret['sex']=user.sex
        ret['tele']=user.tele
        ret['type']=user.type
        ret['marriage']=user.marriage
        ret['birthday']=user.birthday
        ret['live']=user.live
        ret['emile']=user.emile
        ret['education']=user.education
        ret['money']=user.money
        ret['age']=user.age
        ret['work']=user.profession
        ret['wchat']=user.WXchart
        ret['personal']=user.charater
        ret['height']=user.height
        ret['weight']=user.weight
        ret['photo']="http://127.0.0.1:8000/static/"+str(user.photo)
    except IOError:
        ret['code']=1002
        ret['msg']='获取前端数据失败或数据库错误'
    return JsonResponse(ret)
# 修改个人信息
@csrf_exempt
def ChangePersonal(request):
    ret = {'code': 1000, 'msg': None,}
    try:
        email = request.POST.get('email')
        print(email)
        user=models.user.objects.get(emile=email)

        user.name=request.POST.get('name')
        user.tele=request.POST.get('tele')
        user.marriage=request.POST.get('marriage')
        user.live=request.POST.get('live')
        user.education=request.POST.get('education')
        user.money=request.POST.get('money')+"k"
        user.age=request.POST.get('age')
        user.profession=request.POST.get('work')
        user.WXchart=request.POST.get('wchat')
        user.height=request.POST.get('height')+"cm"
        user.weight=request.POST.get('weight')+"kg"
        user.save()
    except IOError:
        ret['code']=1002
        ret['msg']='获取前端数据失败或数据库错误'
    return JsonResponse(ret)
# 修改自我介绍信息
@csrf_exempt
def Change2Personal(request):
    ret = {'code': 1000, 'msg': None,}
    try:
        email = request.POST.get('email')
        print(email)
        user=models.user.objects.get(emile=email)
        user.charater=request.POST.get('personal') 
        user.save()
    except IOError:
        ret['code']=1002
        ret['msg']='获取前端数据失败或数据库错误'
    return JsonResponse(ret)
# 上传用户头像照片
@csrf_exempt
def UploadPersonal(request):
    ret = {'code': 1000, 'msg': None,}
    try:
        email =request.POST.get('data')
        user=models.user.objects.get(emile=email)
        photo =request.FILES.get('photo')
        print(email)
        print(photo)
        user.photo =photo
        user.save()
        # getuser=models.user.objects.get(emile=email)
        # ret['url']=getuser.photo
    except IOError:
        ret['code']=1002
        ret['msg']='获取前端数据失败或数据库错误'
    return JsonResponse(ret)

#会员价格显示
@csrf_exempt
def Vip(request):
    ret = {'code': 1000, 'msg': None,}
    try:
        vip=models.memberprice.objects.all().order_by('-date')[:1]
        print(vip[0].price)
        ret['msg']=vip[0].price

    
    except IOError:
        ret['code']=1002
        ret['msg']='获取前端数据失败或数据库错误'
    return JsonResponse(ret)

# 成为会员
@csrf_exempt
def Bevip(request):
    ret = {'code': 1000, 'msg': None,}
    try:
        email =request.POST.get('user')
        user=models.user.objects.get(emile=email)
        user.type="会员用户"
        user.save()
        ret['msg']='您已成为一缘尊贵会员'
    except IOError:
        ret['code']=1002
        ret['msg']='获取前端数据失败或数据库错误'
    return JsonResponse(ret)

#  获取朋友信息
@csrf_exempt
def GetFriends(request):
    ret = {'code': 1000, 'msg': None,}
    try:
        email =request.POST.get('user')
        friends=models.friends.objects.filter(userid_id=email)
        friend={}
        fList=[]
        print(friends[0].friendid)
        if friends:
        
            for i in friends:
                friper=models.user.objects.get(emile=i.friendid)
                
            
                dict = friper.to_dict()
                dict['photo']="http://127.0.0.1:8000/static/"+str(friper.photo)
                dict['birthday']=str(friper.birthday)
                dict['choose'] = False

# 避免深拷贝
                fList.append(dict.copy())
            
            Json = json.dumps(fList,ensure_ascii=False)
            print(type(Json))
            ret['list']=Json
        else:
            ret['code']=1001
            ret['msg']='快去添加朋友吧'

    except IOError:
        ret['code']=1002
        ret['msg']='获取前端数据失败或数据库错误'
    return JsonResponse(ret)
 

