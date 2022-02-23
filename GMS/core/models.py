from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    token=models.CharField(max_length=150)
    verify=models.BooleanField(default=False)
# erdf7uguih


# class cu_add(models.Model):
#     user = models.ForeignKey(
#         User, on_delete=models.SET_NULL, null=True, blank=True)
#     name = models.CharField(max_length=50)
#     contact = models.CharField(max_length=10)
#     emailid = models.CharField(max_length=50)
#     age = models.CharField(max_length=40)
#     gender = models.CharField(max_length=10, default="")
#     weight = models.CharField(max_length=50)
    

#     def __str__(self):
#         return self.name
class SignUp(models.Model):
    username=models.CharField(max_length=50)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)

class xyz_a(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=50)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    # contact = models.CharField(max_length=10)
    emailid = models.CharField(max_length=50)
    age = models.CharField(max_length=40)
    gender = models.CharField(max_length=10, default="")
    weight = models.CharField(max_length=50)
    height = models.CharField(max_length=50)
    
    
    def __str__(self):
        return self.name

class SendPlanadmin(models.Model):
    name1 = models.CharField(max_length=50,null=True)
    amount = models.CharField(max_length=10,null=True)
    duration = models.CharField(max_length=10,null=True)
    planN = models.CharField(max_length=10,null=True)
