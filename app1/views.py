from django.shortcuts import render
from django.http import HttpResponse
from app1.models import *
from django.db.models.functions import Length
from django.db.models import Q

# Create your views here.
def topic_table(request):
  qlto=Topic.objects.all()
  # Topic.objects.filter(topic_name='Kabaddi').delete()
  d={'Topic':qlto}
  return render(request,'topic_table.html',context=d)

def insert_into_topic(request):
  tn=input('Enter new Topic_name: ')
  nto=Topic.objects.get_or_create(topic_name=tn)[0]
  nto.save()
  return HttpResponse(f'New data <b><u>{tn}</u></b> sccuessfully inserted in topic table')

def webpage(request):
  qlwo=Webpage.objects.all()
  # qlwo=Webpage.objects.order_by('name') 
  # qlwo=Webpage.objects.all().order_by('topic_name')
  # qlwo=Webpage.objects.all().order_by('-name')
  # qlwo=Webpage.objects.all().order_by(Length('name'))
  # qlwo=Webpage.objects.all().order_by(Length('name').desc())
  # qlwo=Webpage.objects.all()[:5:2]
  # qlwo=Webpage.objects.all().order_by(Length('name'))[:5:]
  # qlwo=Webpage.objects.exclude(topic_name='cricket')
  # qlwo=Webpage.objects.exclude(topic_name='cricket').order_by(Length('name'))
  # qlwo=Webpage.objects.exclude(topic_name='cricket').order_by(Length('name'))[1:3:-1]
  # qlwo=Webpage.objects.filter(topic_name='cricket').order_by(Length('name'))
  # qlwo=Webpage.objects.filter(name__startswith='R')
  # qlwo=Webpage.objects.filter(name__endswith='l')
  # qlwo=Webpage.objects.filter(name__contains='H')
  # qlwo=Webpage.objects.filter(name__in=['sunil','dhoni','jorden'])
  # qlwo=Webpage.objects.filter(name__regex='t$')
  # qlwo=Webpage.objects.filter(topic_name='cricket', name__startswith='R')
  # qlwo=Webpage.objects.filter(Q(topic_name='cricket') & Q(name__startswith='R'))
  # qlwo=Webpage.objects.filter(Q(topic_name='cricket') | Q(name__endswith='l'))
  # qlwo=Webpage.objects.filter(Q(topic_name__gt='c') & Q(name__startswith='R'))
  # qlwo=Webpage.objects.filter(Q(topic_name__lt='c') | Q(name__startswith='R'))
  # qlwo=Webpage.objects.filter(Q(topic_name='cricket') | Q(name__startswith='s') & Q(url__contains='app1'))
  # Webpage.objects.filter(name='marrycom').update(url="http://127.0.0.1:8000/admin/marrycom")
  # Webpage.objects.filter(email='xyz@gmail.com').update(email="abc@gmail.com")
  # Webpage.objects.filter(email='xyz@gmail.com').update(email="pqr@gmail.com")
  # Webpage.objects.filter(name='Sunil').update(topic_name="Boxing")
  # Webpage.objects.update_or_create(topic_name='Football',defaults={"email":"pqr@gmail.com"})
  # cto=Topic.objects.get_or_create(topic_name="kabaddi")[0]
  # cto.save()
  # Webpage.objects.update_or_create(name='jorden',defaults={"topic_name":cto, "url": "http://127.0.0.1:8000/jorden/"})
  # Webpage.objects.update_or_create(name='sushil',defaults={"topic_name":cto, "url": "http://127.0.0.1:8000/sushil/"})

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
  # qlao=AccessRecord.objects.filter(id__gt = 1)
  # qlao=AccessRecord.objects.filter(date__gt = '2023-11-2')
  # qlao=AccessRecord.objects.filter(date__year = '2023')
  # qlao=AccessRecord.objects.filter(date__month = '12')
  # qlao=AccessRecord.objects.filter(date__day = '13')
  # qlao=AccessRecord.objects.filter(date__day__gt = '13')
  # qlao=AccessRecord.objects.filter(Q(date__day='13') | Q(auther__gte='p') )
  AccessRecord.objects.all().delete()

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
