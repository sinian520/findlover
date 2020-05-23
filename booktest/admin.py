from django.contrib import admin

# Register your models here.
from.models import user,memberprice,partyapply,partymessage,xinwen,text,friends,userdynamic,comment
class user_admin(admin.ModelAdmin):
    list_display=['name','password','type','tele','live','emile','birthday','age','charater','profession','photo',
                  'WXchart','friendcount','sex','money','education','marriage','status']
    list_filter=['name','type']
    searche_fields=['name','type']
admin.site.register(user,user_admin)
class memberprice_admin(admin.ModelAdmin):
    list_display = ['date','price','people']
admin.site.register(memberprice,memberprice_admin)
class partyapply_admin(admin.ModelAdmin):
    list_display=['time','place','tele','activities','money','Count','holder']
admin.site.register(partyapply,partyapply_admin)
class partymessage_admin(admin.ModelAdmin):
    list_display = ['planA','evaluate','partyid','participant']
admin.site.register(partymessage,partymessage_admin)
class xinwen_admin(admin.ModelAdmin):
    list_display = ['table','subject','count','day']
admin.site.register(xinwen,xinwen_admin)
class text_admin(admin.ModelAdmin):
    list_display = ['img','count','subject','http']
admin.site.register(text,text_admin)
class friends_admin(admin.ModelAdmin):
    list_display = ['friendid','userid']
admin.site.register(friends,friends_admin)
class userdynamic_admin(admin.ModelAdmin):
    list_display = ['time','text','img','userid']
admin.site.register(userdynamic,userdynamic_admin)
class comment_admin(admin.ModelAdmin):
    list_display = ['time','Text','Form_uid','dynamic']
admin.site.register(comment,comment_admin)