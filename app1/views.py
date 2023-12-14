from django.shortcuts import render
from django.http import HttpResponse
from app1.models import *

# Create your views here.
def topic_table(request):
  qlto=Topic.objects.all()
  d={'Topic':qlto}
  return render(request,'topic_table.html',context=d)

def insert_into_topic(request):
  tn=input('Enter new Topic_name: ')
  nto=Topic.objects.get_or_create(topic_name=tn)[0]
  nto.save()
  return HttpResponse(f'New data <b><u>{tn}</u></b> sccuessfully inserted in topic table')

def webpage(request):
  qlwo=Webpage.objects.all()
  d={'Webpage':qlwo}
  return render(request,'webpage.html',context=d)

def insert_into_webpage(request):
  tn=input('Enter Topic_name: ')
  to=Topic.objects.get(topic_name=tn)
  n=input('Enter new name: ')
  u=input('Enter new Url: ')
  e=input('Enter new Email: ')
  nwo=Webpage.objects.get_or_create(topic_name=to,name=n,url=u,email=e)[0]
  nwo.save()
  return HttpResponse(f'New data <b><u>{tn}, {n}, {u}, {e}</u></b> sccuessfully inserted in webpage table')

def accessrecord(request):  
  qlao=AccessRecord.objects.all()
  d={'AccessRecord':qlao}
  return render(request,'accessrecord.html',context=d)


def insert_into_access(request):
  p=int(input('Enter primary key: '))
  wo=Webpage.objects.get(pk=p)
  n=input('Enter new name: ')
  d=input('Enter new date in format "YYYY-MM-DD": ')
  a=input('Enter new auther: ')
  nao=AccessRecord.objects.get_or_create(name=wo,date=d,auther=a)[0]
  nao.save()
  return HttpResponse(f'New data <b><u> {n}, {d}, {a}</u></b> sccuessfully inserted in webpage table')
