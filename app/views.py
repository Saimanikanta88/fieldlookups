import imp
from django.shortcuts import render
from django.db.models.functions import Length
# from django.db.models.functions import Q
# Create your views here.
from app.models import *

def display_topic(request):
    T=Topic.objects.all().order_by(length('topic_name'))
    d={'topics':T}
    return render(request,'display_topic.html',d)

def display_webpage(request):
    W=Webpage.objects.all()
    W=Webpage.objects.all().order_by('topic_name')
    W=Webpage.objects.all().order_by('-topic_name')
    W=Webpage.objects.all().filter(topic_name='carrom').order_by('name')
    W=Webpage.objects.all().filter(topic_name='chess')
    W=Webpage.objects.order_by(Length('topic_name').desc())
    W=Webpage.objects.all()[1:5:]
    W=Webpage.objects.filter(name__startswith='s')
    W=Webpage.objects.filter(name__endswith='n')
    W=Webpage.objects.filter(name__contains='s')
    W=Webpage.objects.filter(name__in=('suman','sai'))
    W=Webpage.objects.filter(name__regex='\w{4}')

    # W=Webpage.objects.filter(name__regex='/w{6}')
    # W=Webpage.objects.filter()
    d={'webpages':W}
    return render(request,'display_webpage.html',d)
    

def accessrecords(request):
    A=Accessrecords.objects.all()
    A=Accessrecords.objects.filter(date__year=2022)
    A=Accessrecords.objects.filter(date__month=10)
    A=Accessrecords.objects.filter(date__day=3)
    A=Accessrecords.objects.filter(date__year__gt=2021)
    A=Accessrecords.objects.filter(date__year__lt=2000)
    A=Accessrecords.objects.filter(date__year__gte=2014)
    d={'accessrecords':A}
    return render(request,'display_accessrecords.html',d)



