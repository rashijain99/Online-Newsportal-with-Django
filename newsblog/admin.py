from django.contrib import admin
from newsblog.models import news , firstsidenews , secondleft , thirdfirst , thirdsecond , fourth , tags , userinfo

class news_admin(admin.ModelAdmin):
    list_display=('news_title','news_desc','news_image')

admin.site.register(news,news_admin)


class firstnews_admin(admin.ModelAdmin):
    list_display=('firstsidenews_title','firstsidenews_image')

admin.site.register(firstsidenews,firstnews_admin)


class secondleft_admin(admin.ModelAdmin):
    list_display=('secondleft_title','secondleft_image')

admin.site.register(secondleft,secondleft_admin)


class thirdfirst_admin(admin.ModelAdmin):
    list_display=('thirdfirst_title','thirdfirst_image')

admin.site.register(thirdfirst,thirdfirst_admin)


class thirdsecond_admin(admin.ModelAdmin):
    list_display=('thirdsecond_title','thirdsecond_image')

admin.site.register(thirdsecond,thirdsecond_admin)



class fourth_admin(admin.ModelAdmin):
    list_display=['fourth_image']

admin.site.register(fourth,fourth_admin)


class tags_admin(admin.ModelAdmin):
    list_display=['tags_title']

admin.site.register(tags,tags_admin)


class userinfo_admin(admin.ModelAdmin):
    list_display=('name', 'title','mobile', 'message', 'date_birth', 'gender','marital_status','addressLine1','addressLine2','state','city')

admin.site.register(userinfo,userinfo_admin)


