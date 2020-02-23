from booktest.models import EmailVerify
from random import randrange
from django.core.mail import send_mail



def get_code(code_length):
    codesourse='123456789990qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    code=''
    for i in range(code_length):
        #随机选择一个字符
        str=codesourse[randrange(0,len(codesourse))]
        code+=str
    return code


def send_email_code(email,sendtype):
    EMAIL_FORM="1755457338@qq.com"


    # 1.创建邮箱验证码对象，保存数据库，用来以后作对比
    # if models.EmailVerify.objects.filter(email=email):
    #     del_obj = models.EmailVerify.objects.get(email=email) # 继承models中的数据库类
    #     del_obj.delete()  # 删除操作
    # else:
    a=EmailVerify()
    a.email=email
    a.sendtype=sendtype
    code=get_code(4)
    a.code=code
    a.save()

    # 2.正式的发邮件功能
    if sendtype==1:
        send_title='欢迎注册一缘婚恋交友网站：'
        send_body='您的验证信息为：'+code
        send_mail(send_title,send_body,EMAIL_FORM,[email])

