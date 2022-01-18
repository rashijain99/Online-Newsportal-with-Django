from django.db import models
from django.shortcuts import render , redirect
from django.http import HttpResponse , HttpResponseRedirect
from newsblog.models import news  ,firstsidenews , secondleft ,thirdfirst , thirdsecond , fourth , tags, userinfo
from newsblog.forms import userForm




def home(request):
    newsdata =  news.objects.all()
    firstnewsdata  =  firstsidenews.objects.all()
    secondleftdata = secondleft.objects.all().order_by('secondleft_title')[:4]
    thirdfirstdata = thirdfirst.objects.all().order_by('thirdfirst_title')
    thirdseconddata = thirdsecond.objects.all().order_by('thirdsecond_title')
    fourthdata = fourth.objects.all()
    tagsdata = tags.objects.all()


    data ={
        'news': newsdata,
        'firstnews' : firstnewsdata,
        'secondleftdata' : secondleftdata,
        'thirdfirstdata' : thirdfirstdata,
        'thirdseconddata': thirdseconddata,
        'fourthdata' : fourthdata,
        'tagsdata': tagsdata
    }
    return render(request,"home.html", data)


def detailnews(request,newsid):
    detailnews = news.objects.get(id=newsid)
    data={
        'detailnews': detailnews
    }
    return render(request,'detailnews.html',data)    



def notfoundpage(request):
    firstnewsdata  =  firstsidenews.objects.all()
    data ={
        'firstnews' : firstnewsdata,
    }
    return render(request,"404.html",data)


def about(request):
    firstnewsdata  =  firstsidenews.objects.all()
    data ={
        'firstnews' : firstnewsdata,
    }
    return render(request,"about.html",data)


def contact(request):
    fn = userForm(request.POST) 

    if request.method == 'POST' :
        name_a = request.POST.get('name')
        title_a  = request.POST.get('title')
        mobile_a  = request.POST.get('mobile')
        message_a = request.POST.get('message')
        dob = request.POST.get('date_birth')

        gender_a = request.POST.get('gender')
        marital_status_a = request.POST.get('marital_status')
        addressLine1_a = request.POST.get('addressLine1')
        addressLine2_a = request.POST.get('addressLine2')
        state_a = request.POST.get('state')
        city_a = request.POST.get('city')
        

        xyz=userinfo(name= name_a, title = title_a , message = message_a, mobile= mobile_a , date_birth= dob , gender =gender_a , marital_status = marital_status_a, addressLine1 =addressLine1_a , addressLine2 = addressLine2_a, state = state_a, city =city_a)
        xyz.save()
        return redirect('contact')


       

    firstnewsdata  =  firstsidenews.objects.all()
    data ={
        'firstnews' : firstnewsdata,
        'form' :fn
    }

    return render(request,"contact.html",data)


def singlepage(request):
    newsdata =  news.objects.all()
    firstnewsdata  =  firstsidenews.objects.all()
    secondleftdata = secondleft.objects.all().order_by('secondleft_title')[:4]
    thirdfirstdata = thirdfirst.objects.all().order_by('thirdfirst_title')
    thirdseconddata = thirdsecond.objects.all().order_by('thirdsecond_title')
    fourthdata = fourth.objects.all()
    tagsdata = tags.objects.all()


    data ={
        'news': newsdata,
        'firstnews' : firstnewsdata,
        'secondleftdata' : secondleftdata,
        'thirdfirstdata' : thirdfirstdata,
        'thirdseconddata': thirdseconddata,
        'fourthdata' : fourthdata,
        'tagsdata': tagsdata
    }
    return render(request,"single_page.html",data)
    