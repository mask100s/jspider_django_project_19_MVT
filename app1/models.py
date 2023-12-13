from django.db import models

# Create your models here.
class Dept(models.Model):
  deptno=models.PositiveIntegerField(primary_key=True)
  dname=models.CharField(max_length=14)
  loc=models.CharField(max_length=13)

  # def __str__ (self):
  #   return [self.dname,self.loc]

class Emp(models.Model):
  empno=models.PositiveIntegerField(primary_key=True)
  ename=models.CharField(max_length=10)
  job=models.CharField(max_length=9)
  mgr=models.PositiveIntegerField()
  hiredate=models.DateField()     
  sal=models.PositiveIntegerField()
  comm=models.PositiveIntegerField(blank=True,null=True)
  deptno=models.ForeignKey(Dept,on_delete=models.CASCADE)

  # def __str__ (self):
  #   return [self.ename,self.job]
  
class Salgrade(models.Model):
  grade=models.PositiveIntegerField()
  losal=models.PositiveIntegerField()
  hisal=models.PositiveIntegerField()

class Bonus(models.Model):
  pass