from tkinter import S
from django.contrib import admin
from .models import TProfile ,Bmi,sendPlan

# Register your models here.
@admin.register(TProfile)
class TProfileAdmin(admin.ModelAdmin):
    list_display=['id','token','user','verify']
# @admin.register(SignUpForm)
# class RegisteredAdmin(admin.ModelAdmin):
#     list_display=['id','username','first_name','last_name','email','password']

# admi
# admin.site.register(cu_add)
class BmiAdmin(admin.ModelAdmin):
    list_display = ('age', 'weight', 'height', 'bmi', 'date')

admin.site.register(Bmi, BmiAdmin)
class sendPlanAdmin(admin.ModelAdmin):
    list_display = ('name1', 'amount', 'duration','planN ')

admin.site.register(sendPlan)

