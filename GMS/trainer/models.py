from django.db import models
from django.contrib.auth.models import User 
from .forms import SignUpForm
# Create your models here.
# 
class search(models.Model):
   
   query=models.CharField(max_length=150)
    
class TProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    token=models.CharField(max_length=150)
    verify=models.BooleanField(default=False)
    
# erdf7uguih
class Bmi(models.Model):
    
    age= models.CharField(max_length=10,null=True, blank=True)
    
    weight = models.FloatField()
   
    height = models.FloatField()
    bmi = models.FloatField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.username
class sendPlan(models.Model):
    name1 = models.CharField(max_length=50,null=True)
    amount = models.CharField(max_length=10,null=True)
    duration = models.CharField(max_length=10,null=True)
    planN = models.CharField(max_length=10,null=True)
