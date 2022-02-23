from django.contrib import admin
from .models import Profile,xyz_a, SignUp,SendPlanadmin
# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display=['id','token','user','verify']
@admin.register(xyz_a)
class xyz_aAdmin(admin.ModelAdmin):
    list_display=('id','name','fname','fname','emailid','age','gender','weight','height')
   

# admin.site.register(cu_add)
# admin.site.register(xyz_a)
@admin.register(SignUp)
class SignUpFormAdmin(admin.ModelAdmin):
    list_display=['id','username','email','first_name','last_name']
class SendPlanadminAdmin(admin.ModelAdmin):
    list_display = ('name1', 'amount', 'duration','planN ')

admin.site.register(SendPlanadmin)

