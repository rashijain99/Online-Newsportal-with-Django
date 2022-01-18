from django.contrib.admin.sites import DefaultAdminSite
from django.db import models 
from tinymce import models as tinymce_models
from newswebsite import settings

class news(models.Model):
    news_title = models.CharField(max_length=100)
    news_desc = tinymce_models.HTMLField()
    news_image = models.FileField(upload_to="news/", max_length=250, null=True,default=None)


class firstsidenews(models.Model):
    firstsidenews_title = models.CharField(max_length=100)
    firstsidenews_image = models.FileField(upload_to="firstsidenews/", max_length=250, null=True,default=None)


class secondleft(models.Model):
    secondleft_title = models.CharField(max_length=100)
    secondleft_image = models.FileField(upload_to="secondleft/", max_length=250, null=True,default=None)


class thirdfirst(models.Model):
    thirdfirst_title = models.CharField(max_length=100)
    thirdfirst_image = models.FileField(upload_to="thirdfirst/", max_length=250, null=True,default=None)


class thirdsecond(models.Model):
    thirdsecond_title = models.CharField(max_length=100)
    thirdsecond_image = models.FileField(upload_to="thirdsecond/", max_length=250, null=True,default=None)    


class fourth(models.Model):
    fourth_image = models.FileField(upload_to="fourth/", max_length=250, null=True,default=None) 


class tags(models.Model):
    tags_title = models.CharField(max_length=50)                  



TITLE_CHOICES = [
    ('MR', 'Mr.'),
    ('MRS', 'Mrs.'),
    ('MS', 'Ms.'),
]

gender_CHOICES = [
    ('MALE', 'Male'),
    ('FEMALE', 'Female'),
    ('OTHER', 'Other'),
    ]

MARITAL_CHOICES = [
    ('MARRIED', 'Married'),
    ('SINGLE', 'Single'),
    ('WIDOWED', 'Widowed'),
    ('DIVORCED', 'Divorced'),
    ]    


class userinfo(models.Model):
    name = models.CharField(null=True, blank=True,max_length=100,default=None)
    title = models.CharField(null=True, blank=True,max_length=3, choices=TITLE_CHOICES,default=None)
    mobile = models.CharField(null=True, blank=True,max_length=15,default=None)
    message = models.CharField(null=True, blank=True,max_length=200,default=None)
    date_birth = models.DateField(blank=True, null=True, help_text='Please enter DATE in Format - YYYY-MM-DD ')

    gender = models.CharField(null=True, blank=True,choices=gender_CHOICES, default= 'MALE', max_length=100)
    marital_status = models.CharField(null=True, blank=True,choices=MARITAL_CHOICES, default='SINGLE', max_length=100)
    addressLine1 = models.CharField(null=True, blank=True, max_length=200)
    addressLine2 = models.CharField(null=True, blank=True, max_length=200)
    state = models.CharField(null=True, blank=True, max_length=100)
    city = models.CharField(null=True, blank=True, max_length=100)
   

