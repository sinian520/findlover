# coding=utf-8
from django.db import models
# model转字典
from django.db.models.fields import DateTimeField
from django.db.models.fields.related import ManyToManyField
# Create your models here.

# 用户表
class user(models.Model):
    name = models.CharField(max_length=20,verbose_name='昵称')
    password = models.CharField(max_length=20,verbose_name='密码')#密码
    type = models.CharField(max_length=20,verbose_name='用户类型')#用户类型
    tele = models.CharField(max_length=12,verbose_name='电话')#电话
    live = models.CharField(max_length=50,verbose_name='所在地',null=True,blank=True)#所在地
    emile = models.CharField(max_length=20,verbose_name='邮箱')#邮箱
    birthday = models.DateField(verbose_name='生日',null=True,blank=True)#生日
    age = models.CharField(verbose_name='年龄',null=True,blank=True,max_length=20)#年龄
    charater = models.CharField(max_length=500,verbose_name='自我介绍',null=True,blank=True)#自我介绍
    profession = models.CharField(max_length=20,verbose_name='职业',null=True,blank=True)#职业
    # 这里的upload_to是指定图片存储的文件夹名称，上传文件之后会自动创建
    photo = models.ImageField(upload_to='img',null=True,blank=True)#个人照片
    WXchart = models.CharField(max_length=20,verbose_name='微信',null=True,blank=True)#微信号
    friendcount = models.CharField(verbose_name='好友数',max_length=20,null=True,blank=True)#好友个数
    sex = models.CharField(max_length=12,verbose_name='性别')#性别
    money = models.CharField(max_length=20,verbose_name='月薪',null=True,blank=True)#月薪
    education = models.CharField(max_length=12,verbose_name='学历',null=True,blank=True)#学历
    marriage = models.CharField(max_length=12,verbose_name='婚姻状况',null=True,blank=True)#婚姻状况
    status = models.BooleanField(max_length=20,verbose_name='在线状态')#在线状态
    height = models.CharField(max_length=12,verbose_name='身高',null=True,blank=True)#身高
    weight = models.CharField(max_length=12,verbose_name='体重',null=True,blank=True)#体重

    def __int__(self):
        return self.id

    def to_dict(self, fields=None, exclude=None):
        data = {}
        for f in self._meta.concrete_fields + self._meta.many_to_many:
            value = f.value_from_object(self)
 
            if fields and f.name not in fields:
                continue
 
            if exclude and f.name in exclude:
                continue
 
            if isinstance(f, ManyToManyField):
                value = [ i.id for i in value ] if self.pk else None
 
            # if isinstance(f, DateTimeField):
            #     value = value.strftime('%Y-%m-%d %H:%M:%S') if value else None
 
            data[f.name] = value
 
        return data
    
    


#会员价格表
class memberprice(models.Model):
    date = models.DateTimeField(auto_now=True,verbose_name='时间')#自动获取当前时间
    price = models.IntegerField(verbose_name='价格')#价格
    people = models.CharField(max_length=20,verbose_name='设定人')#设定人

    def __int__(self):
        return self.id

# 线下活动申请表
class partyapply(models.Model):
    time= models.DateTimeField(verbose_name='活动时间')#时间
    place = models.CharField(max_length=20,verbose_name='活动地点')#地点
    tele = models.CharField(max_length=20,verbose_name='活动名称')#举办方联系电话
    activities= models.TextField(max_length=200,verbose_name='内容介绍')#活动内容
    money= models.IntegerField(verbose_name='资金/每人')#资金/每人
    Count= models.IntegerField(verbose_name='参与人数')#活动人数
    status = models.BooleanField(max_length=20,verbose_name='活动状态')#在线状态
    holder = models.ForeignKey("user", on_delete=models.CASCADE,verbose_name='举办人')#举办人
   
    def __int__(self):
        return self.id
    def to_dict(self, fields=None, exclude=None):
        data = {}
        for f in self._meta.concrete_fields + self._meta.many_to_many:
            value = f.value_from_object(self)
 
            if fields and f.name not in fields:
                continue
 
            if exclude and f.name in exclude:
                continue
 
            if isinstance(f, ManyToManyField):
                value = [ i.id for i in value ] if self.pk else None
 
            # if isinstance(f, DateTimeField):
            #     value = value.strftime('%Y-%m-%d %H:%M:%S') if value else None
 
            data[f.name] = value
 
        return data

#线下活动信息表
class partymessage(models.Model):
    planA = models.CharField(max_length=12,verbose_name='评分',null=True,blank=True,default='')#参与者联系电话
    evaluate= models.TextField(max_length=12,verbose_name='活动评价',null=True,blank=True)#活动评价
    partyid = models.ForeignKey("partyapply", on_delete=models.CASCADE,verbose_name='活动编号')#活动编号
    participant = models.ForeignKey("user", on_delete=models.CASCADE,verbose_name='参与人')#参与人

    def __int__(self):
        return self.id
    def to_dict(self, fields=None, exclude=None):
        data = {}
        for f in self._meta.concrete_fields + self._meta.many_to_many:
            value = f.value_from_object(self)
 
            if fields and f.name not in fields:
                continue
 
            if exclude and f.name in exclude:
                continue
 
            if isinstance(f, ManyToManyField):
                value = [ i.id for i in value ] if self.pk else None
 
            # if isinstance(f, DateTimeField):
            #     value = value.strftime('%Y-%m-%d %H:%M:%S') if value else None
 
            data[f.name] = value
 
        return data
#心里测试题表
class text(models.Model):
    img = models.CharField(max_length=200,verbose_name='图片')#图片
    count= models.IntegerField(verbose_name='测试人数')#测试人数
    subject= models.CharField(max_length=20,verbose_name='标题')#标题
    http= models.TextField(max_length=20,verbose_name='测试连接')#测试连接

    def __int__(self):
        return self.id
#朋友表
class friends(models.Model):
    friendid =  models.CharField(max_length=20,verbose_name='朋友')#朋友编号
    userid = models.ForeignKey("user", on_delete=models.CASCADE,verbose_name='用户号')#用户号
    #name= models.TextField(max_length=12)#昵称
    #img = models.CharField(max_length=20)#朋友图片
    def __int__(self):
        return self.id

#用户动态表
class userdynamic(models.Model):
    time = models.DateTimeField(auto_now=True,verbose_name='发表时间')#发表时间
    title= models.CharField(max_length=200,verbose_name='标题',default='')#标题
    text= models.TextField(max_length=500,verbose_name='内容')#发表内容
    img =models.ImageField(upload_to='img',null=True,verbose_name='图片',blank=True)#图片
    userid = models.ForeignKey("user",on_delete=models.CASCADE,verbose_name='用户号')

    def __int__(self):
        return self.id
    def to_dict(self, fields=None, exclude=None):
        data = {}
        for f in self._meta.concrete_fields + self._meta.many_to_many:
            value = f.value_from_object(self)
 
            if fields and f.name not in fields:
                continue
 
            if exclude and f.name in exclude:
                continue
 
            if isinstance(f, ManyToManyField):
                value = [ i.id for i in value ] if self.pk else None
 
            # if isinstance(f, DateTimeField):
            #     value = value.strftime('%Y-%m-%d %H:%M:%S') if value else None
 
            data[f.name] = value
 
        return data

#用户动态评论表
class comment(models.Model):
    time = models.DateTimeField(auto_now=True,verbose_name='发表时间')#发表时间
    Text= models.TextField(max_length=200,verbose_name='评论内容')#评论内容
    Form_uid = models.CharField(max_length=20,verbose_name='评论用户')#评论用户
    dynamic = models.ForeignKey("userdynamic",on_delete=models.CASCADE,verbose_name='动态编号')#动态编号
    
    def __int__(self):
        return self.id
    def to_dict(self, fields=None, exclude=None):
        data = {}
        for f in self._meta.concrete_fields + self._meta.many_to_many:
            value = f.value_from_object(self)
 
            if fields and f.name not in fields:
                continue
 
            if exclude and f.name in exclude:
                continue
 
            if isinstance(f, ManyToManyField):
                value = [ i.id for i in value ] if self.pk else None
 
            # if isinstance(f, DateTimeField):
            #     value = value.strftime('%Y-%m-%d %H:%M:%S') if value else None
 
            data[f.name] = value
 
        return data

#恋爱信息表
class xinwen(models.Model):
    table = models.CharField(max_length=200,verbose_name='文章标题')#文章标题
    subject = models.TextField(max_length = 500,verbose_name='内容')#内容
    count=models.IntegerField(verbose_name='浏览次数',null=True,blank=True)#浏览次数
    day = models.DateField(auto_now=True,verbose_name='发表时间')  # 时间
    img =models.ImageField(upload_to='img',null=True,verbose_name='图片',blank=True)#图片
    userid = models.ForeignKey("user",on_delete=models.CASCADE,verbose_name='用户号' ,default='')
    def __int__(self):
        return self.id
    def to_dict(self, fields=None, exclude=None):
        data = {}
        for f in self._meta.concrete_fields + self._meta.many_to_many:
            value = f.value_from_object(self)
 
            if fields and f.name not in fields:
                continue
 
            if exclude and f.name in exclude:
                continue
 
            if isinstance(f, ManyToManyField):
                value = [ i.id for i in value ] if self.pk else None
 
            # if isinstance(f, DateTimeField):
            #     value = value.strftime('%Y-%m-%d %H:%M:%S') if value else None
 
            data[f.name] = value
 
        return data


# 用户token表
class UserToken(models.Model):
    user = models.CharField(max_length=20,verbose_name='邮箱')#邮箱
    token=models.CharField(max_length=100,verbose_name='token')#登录验证

# 用户邮箱验证表
class EmailVerify(models.Model):
    code = models.CharField(max_length=20,verbose_name='邮箱验证码')
    email=models.CharField(max_length=100,verbose_name='验证码邮箱')
    sendtype=models.IntegerField(choices=((1,'register'),(2,'forget'),(3,'change')),verbose_name='验证码邮箱')
    time=models.DateTimeField(auto_now=True,verbose_name='操作时间')