from django.shortcuts import render
from app1.models import *

# Create your views here.
def emp_table(request):
  qleo=Emp.objects.all()
  d={'emp':qleo}
  return render(request,'emp_table.html',context=d)

def dept_table(request):
  qldo=Dept.objects.all()
  d={'dept':qldo}
  return render(request,'dept_table.html',context=d)

def salgrade_table(request):
  qlso=Salgrade.objects.all()
  d={'salgrade':qlso}
  return render(request,'salgrade_table.html',context=d)

def bonus_table(request):
  qlbo=Bonus.objects.all()
  d={'bonus':qlbo}
  return render(request,'bonus_table.html',context=d)