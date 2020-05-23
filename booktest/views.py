from django.shortcuts import render
from .models import user,memberprice,partyapply,partymessage,xinwen,text,friends,userdynamic,comment,UserToken,EmailVerify
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
import datetime

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
        ret['photo']="http://127.0.0.1:8000/media/"+str(user.photo)
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
# 添加朋友
@csrf_exempt
def AddFriend(request):
    ret = {'code': 1000, 'msg': None,}
    try:
        userid=request.POST.get('userid')
        friendid=request.POST.get('friendid')
        

        # 还不是朋友
        user=models.user.objects.get(emile=userid)
        friend=models.user.objects.get(id=friendid)
        # 检查是否已经是朋友
        check=models.friends.objects.filter(userid=user,friendid=friend.emile)
        if check:
            ret['code']=1001
            ret['msg']='你们已经是朋友，请在朋友管理中查看'
        else:
            a=friends()
            a.friendid=friend.emile
            a.userid=user
            a.save()
            ret['msg']="已成功添加朋友"
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
                dict['photo']="http://127.0.0.1:8000/media/"+str(friper.photo)
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
 # 提交恋爱信息
@csrf_exempt
def UploadShowlove(request):
    ret = {'code': 1000, 'msg': None,}
    try:
        email =request.POST.get('user')
        table =request.POST.get('table')
        subject =request.POST.get('subject')
        img =request.FILES.get('file')
        print(img)
        a=xinwen()
        a.table=table
        a.subject=subject
        a.userid_id=email
        a.img=img
        a.count=0
        a.save()
        ret['msg']='发布成功'
    except IOError:
        ret['code']=1002
        ret['msg']='获取前端数据失败或数据库错误'
    return JsonResponse(ret)
 # 展示恋爱信息
@csrf_exempt
def Showlove(request):
    ret = {'code': 1000, 'msg': None,}
    try:
        hot=models.xinwen.objects.order_by("-count")[:5]
        new=models.xinwen.objects.order_by("-day")[:5]
        allshow=models.xinwen.objects.all()
        hList=[]
        nList=[]
        count=1
        if hot:
            for i in hot:
                dict = i.to_dict()

                dict['img']="http://127.0.0.1:8000/media/"+str(i.img)
                dict['day']=str(i.day)
                dict['pxid']=count
                count=count+1
                hList.append(dict.copy())
            # 字典转字符串
            Json = json.dumps(hList,ensure_ascii=False)
            print(Json)
            ret['hot']=Json
        count=1
        if new:
            for i in new:
                dict = i.to_dict()
                dict['img']="http://127.0.0.1:8000/media/"+str(i.img)
                dict['day']=str(i.day)
                dict['pxid']=count
                count=count+1
                nList.append(dict.copy())

            
            Json = json.dumps(nList,ensure_ascii=False)
            print(Json)
            ret['new']=Json
        if allshow:
            for i in allshow:
                dict = i.to_dict()

                dict['img']="http://127.0.0.1:8000/media/"+str(i.img)
                dict['day']=str(i.day)
                hList.append(dict.copy())
            # 字典转字符串
            Json = json.dumps(hList,ensure_ascii=False)
            print(Json)
            ret['allshow']=Json
        ret['msg']='发布成功'
    except IOError:
        ret['code']=1002
        ret['msg']='获取前端数据失败或数据库错误'
    return JsonResponse(ret)
# 恋爱展示送祝福
@csrf_exempt
def AddCount(request):
    ret = {'code': 1000, 'msg': None,}
    try:
        xwid=request.POST.get('id')
        tiao=models.xinwen.objects.get(id=xwid)
        tiao.count+=1
        print(tiao.count)
        tiao.save()
        ret['msg']='祝福已送到'
    except IOError:
        ret['code']=1002
        ret['msg']='获取前端数据失败或数据库错误'
    return JsonResponse(ret)
# 发布线下活动信息
@csrf_exempt
def Activeapply(request):
    ret = {'code': 1000, 'msg': None,}
    try:
        name=request.POST.get('name')
        region=request.POST.get('region')
        date=request.POST.get('date')
        money=request.POST.get('money')
        count=request.POST.get('count')
        desc=request.POST.get('desc')
        email=request.POST.get('user')
        a=partyapply()
        a.tele=name
        a.place=region
        a.time=date
        a.money=money
        a.Count=count
        a.activities=desc
        a.status=True
        user=models.user.objects.get(emile=email)
        a.holder=user
        a.save()
        ret['msg']='已成功发布，可在线下活动版块查看'
    except IOError:
        ret['code']=1002
        ret['msg']='获取前端数据失败或数据库错误'
    return JsonResponse(ret)
 # 展示线下活动信息
@csrf_exempt
def Showactive(request):
    ret = {'code': 1000, 'msg': None,}
    try:
        nList=[]
        oList=[]
        myList=[]
        myattend=[]
        email=request.POST.get('user')
        user=models.user.objects.get(emile=email)
        attendinfo=models.partymessage.objects.filter(participant=user)
        info=models.partyapply.objects.all()
        # 用户参加的所有活动

        print(attendinfo)
        if attendinfo and info:
            for j in attendinfo:
                for i in info:
                    if j.partyid==i:
                        dict = i.to_dict()
                        time_str =i.time.strftime('%Y-%m-%d %H:%M')
                        dict['time']=time_str
                        dict['name']=i.holder.name
                        # 判断是否评价
                        if j.evaluate:
                            dict['evaluate']='已评论'
                        else:
                            dict['evaluate']='未评论'
                        myattend.append(dict.copy())     
        ret['attend']= json.dumps(myattend,ensure_ascii=False)


        if info:
            for i in info:
                # 判断活动是否过期，改变states
                nowTime_str = datetime.datetime.now().strftime('%Y-%m-%d') 
                time =i.time.strftime('%Y-%m-%d')
                time_str =i.time.strftime('%Y-%m-%d %H:%M')
                if nowTime_str>time:
                    i.status=False
                    dict = i.to_dict()
                    dict['time']=time_str
                    dict['name']=i.holder.name
                    oList.append(dict.copy())
                    # dict['evaluate']=attendinfo.evaluate
                    
                else:
                    dict = i.to_dict()
                    dict['time']=time_str
                    dict['name']=i.holder.name
                    nList.append(dict.copy())
                if i.holder==user:
                    dict = i.to_dict()
                    dict['time']=time_str
                    dict['name']=i.holder.name
                    myList.append(dict.copy())       
            # 字典转字符串
            ret['old']= json.dumps(oList,ensure_ascii=False)
            ret['new']=json.dumps(nList,ensure_ascii=False)
            ret['my']=json.dumps(myList,ensure_ascii=False)
            ret['msg']='发布成功'
        

    except IOError:
        ret['code']=1002
        ret['msg']='获取前端数据失败或数据库错误'
    return JsonResponse(ret)
#参加活动
@csrf_exempt
def AttendActive(request):
    ret = {'code': 1000, 'msg': None,}
    try:
        email=request.POST.get('user')
        partyid=request.POST.get('partyid')
        user=models.user.objects.get(emile=email)
        party=models.partyapply.objects.get(id=partyid)
        a=partymessage()
        a.partyid=party
        a.participant=user
        a.save()
        ret['msg']='报名成功'
    except IOError:
        ret['code']=1002
        ret['msg']='获取前端数据失败或数据库错误'
    return JsonResponse(ret)
#获取评价
@csrf_exempt
def GetEvaluate(request):
    ret = {'code': 1000, 'msg': None,}
    try:
        myattend=[]
        partyid=request.POST.get('id')
        party=models.partyapply.objects.get(id=partyid)
        attendinfo=models.partymessage.objects.filter(partyid=party)
        
        if attendinfo:
            for i in attendinfo:
                print(i.id)
                if i.evaluate:
                    dict = i.to_dict()
                    dict['name']=i.participant.name
                    dict['partyid']=i.partyid.id
                    myattend.append(dict.copy())     
        ret['evaluate']= json.dumps(myattend,ensure_ascii=False)
        ret['msg']='成功获取评价'
    except IOError:
        ret['code']=1002
        ret['msg']='获取前端数据失败或数据库错误'
    return JsonResponse(ret)
#用户进行评价
@csrf_exempt
def PostEvaluate(request):
    ret = {'code': 1000, 'msg': None,}
    try:
        partyid=request.POST.get('partyid')
        email=request.POST.get('user')
        rate=request.POST.get('rate')
        evaluate=request.POST.get('evaluate')
        user=models.user.objects.get(emile=email)
        party=models.partyapply.objects.get(id=partyid)
        attendinfo=models.partymessage.objects.get(partyid=party,participant=user)
        print(attendinfo)
        if attendinfo:
            attendinfo.planA=rate
            attendinfo.evaluate=evaluate
            attendinfo.save()
        ret['msg']='评价完成'
    except IOError:
        ret['code']=1002
        ret['msg']='获取前端数据失败或数据库错误'
    return JsonResponse(ret)
# 显示参与活动用户
@csrf_exempt
def GetActiveUser(request):
    ret = {'code': 1000, 'msg': None,}
    try:
        user=[]
        partyid=request.POST.get('id')
        party=models.partyapply.objects.get(id=partyid)
        attendinfo=models.partymessage.objects.filter(partyid=party)
        print(attendinfo)
        if attendinfo:
           for i in attendinfo:
                print(i.participant.tele)
                dict ={}
                dict['age']=i.participant.age
                dict['name']=i.participant.name
                dict['tele']=i.participant.tele
                dict['profession']=i.participant.age
                dict['sex']=i.participant.age
                dict['live']=i.participant.live
                dict['emile']=i.participant.emile
                user.append(dict.copy())  

        ret['user']= json.dumps(user,ensure_ascii=False)   
    except IOError:
        ret['code']=1002
        ret['msg']='获取前端数据失败或数据库错误'
    return JsonResponse(ret)
# 显示用户信息
@csrf_exempt
def HomeUser(request):
    ret = {'code': 1000, 'msg': None,}
    try:
        # 会员用户
        vip=[]
        ordinary=[]
        email=request.POST.get('user')
        print(email)
        oneuser=models.user.objects.get(emile=email)
        print(oneuser.sex)
        if oneuser.sex=='女':
            vipuser=models.user.objects.filter(type="会员用户",sex='男').order_by('-id')
            user=models.user.objects.filter(sex='男')
        else:
            vipuser=models.user.objects.filter(type="会员用户",sex='女').order_by('-id')
            user=models.user.objects.filter(sex='女')
        
        print(vipuser)
        if vipuser:
           for i in vipuser:
                dict = {}
                dict['id']=i.id
                dict['photo']="http://127.0.0.1:8000/media/"+str(i.photo)
                dict['age']=i.age
                dict['marriage']=i.marriage
                vip.append(dict.copy())  
        ret['vip']= json.dumps(vip,ensure_ascii=False)  
        if user:
           for i in user:
                dict = {}
                dict['id']=i.id
                dict['photo']="http://127.0.0.1:8000/media/"+str(i.photo)
                dict['age']=i.age
                dict['marriage']=i.marriage
                dict['live']=i.live
                dict['profession']=i.profession
                dict['charater']=i.charater
                dict['education']=i.education
                ordinary.append(dict.copy())  
        ret['ordinary']= json.dumps(ordinary,ensure_ascii=False)    
    except IOError:
        ret['code']=1002
        ret['msg']='获取前端数据失败或数据库错误'
    return JsonResponse(ret)
# 首页送玫瑰
@csrf_exempt
def AddUserCount(request):
    ret = {'code': 1000, 'msg': None,}
    try:
        userid=request.POST.get('id')
        who=models.user.objects.get(id=userid)
        count=int(who.friendcount)
        count=+1
        who.friendcount=str(count)
        who.save()
        ret['msg']='玫瑰已送到'
    except IOError:
        ret['code']=1002
        ret['msg']='获取前端数据失败或数据库错误'
    return JsonResponse(ret)
# 获取情感求助信息
@csrf_exempt
def AskHelp(request):
    ret = {'code': 1000, 'msg': None,}
    try:
        askList=[]
        userdy=models.userdynamic.objects.all()
        if userdy:
           for i in userdy:
                time_str =i.time.strftime('%Y-%m-%d %H:%M:%S')
                dict = i.to_dict()
                dict['img']="http://127.0.0.1:8000/media/"+str(i.img)
                dict['time']=time_str
                dict['name']=i.userid.name
                dict['type']=i.userid.type
                dict['photo']="http://127.0.0.1:8000/media/"+str(i.userid.photo)
                askList.append(dict.copy())  
        ret['askList']= json.dumps(askList,ensure_ascii=False)    
        ret['msg']='成功'
    except IOError:
        ret['code']=1002
        ret['msg']='获取前端数据失败或数据库错误'
    return JsonResponse(ret)
# 用户发表帖子
@csrf_exempt
def PostHelp(request):
    ret = {'code': 1000, 'msg': None,}
    try:
        email =request.POST.get('user')
        user=models.user.objects.get(emile=email)
        title =request.POST.get('title')
        desc =request.POST.get('desc')
        a=userdynamic()
        a.title=title
        a.text=desc
        a.userid=user
        a.save()
        ret['msg']='帖子发布成功'
    except IOError:
        ret['code']=1002
        ret['msg']='获取前端数据失败或数据库错误'
    return JsonResponse(ret)
# 情感帮助回复
@csrf_exempt
def PostReponse(request):
    ret = {'code': 1000, 'msg': None,}
    try:
        email =request.POST.get('user')
        dyID =request.POST.get('dyID')
        reponse =request.POST.get('reponse')
        dynamic=models.userdynamic.objects.get(id=dyID)
        a=comment()
        a.Text=reponse
        a.Form_uid=email
        a.dynamic=dynamic
        a.save()
        ret['msg']='帖子发布成功'
    except IOError:
        ret['code']=1002
        ret['msg']='获取前端数据失败或数据库错误'
    return JsonResponse(ret)
# 获取回复显示
@csrf_exempt
def Reponseshow(request):
    ret = {'code': 1000, 'msg': None,}
    try:
        one=[]
        userdynamicid=request.POST.get('id')
        obj=models.userdynamic.objects.get(id=userdynamicid)
        comment=models.comment.objects.filter(dynamic=obj)
        
        if comment:
            for i in comment:
                dict = i.to_dict()
                user=models.user.objects.get(emile=i.Form_uid)
                time_str =i.time.strftime('%Y-%m-%d %H:%M:%S')
                dict['photo']="http://127.0.0.1:8000/media/"+str(user.photo)
                dict['time']=time_str
                dict['name']=user.name
                one.append(dict.copy())     
        ret['comment']= json.dumps(one,ensure_ascii=False)
        ret['msg']='成功获取评价'
    except IOError:
        ret['code']=1002
        ret['msg']='获取前端数据失败或数据库错误'
    return JsonResponse(ret)
# 心理测试
@csrf_exempt
def GetText(request):
    ret = {'code': 1000, 'msg': None,}
    try:
        List=[]
        obj=models.text.objects.all()
        if obj:
           for i in obj:
                dict={}
                dict['img']=i.img
                dict['count']=i.count
                dict['subject']=i.subject
                dict['http']=i.http
                List.append(dict.copy())  
        ret['List']= json.dumps(List,ensure_ascii=False)    
        ret['msg']='成功'
    except IOError:
        ret['code']=1002
        ret['msg']='获取前端数据失败或数据库错误'
    return JsonResponse(ret)