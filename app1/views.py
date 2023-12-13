from django.shortcuts import render
from app1.models import *

# Create your views here.
def topic_table(request):
  qlto=Topic.objects.all()
  d={'Topic':qlto}
  return render(request,'topic_table.html',context=d)

def webpage(request):
  qlwo=Webpage.objects.all()
  d={'Webpage':qlwo}
  return render(request,'webpage.html',context=d)