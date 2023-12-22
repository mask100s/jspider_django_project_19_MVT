from django.shortcuts import render
from django.http import HttpResponse
from app1.models import *

# Create your views here.
def topic(request):
  qlto=Topic.objects.all()
  d={'Topic':qlto}
  return render(request,'topic.html',context=d)

# def insert_into_topic(request):
#   tn=input('Enter new Topic_name: ')
#   nto=Topic.objects.get_or_create(topic_name=tn)[0]
#   nto.save()
#   return HttpResponse(f'New data <b><u>{tn}</u></b> sccuessfully inserted in topic table')