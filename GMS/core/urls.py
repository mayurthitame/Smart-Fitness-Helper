from django.urls import path
from core import views
from . import views
from .views import Home,SignUpView,account_verify,SignInView,Contact,About,myplan, sendplanadmin,viewplan
urlpatterns=[
path('',Home.as_view(),name='home'),
path("normal", views.normal, name='normal'),
    
path('sign-up/',SignUpView.as_view(),name='sign-up'),
path('account-verify/<slug:token>',account_verify,name='account_verify'),
path('sign-in/',SignInView.as_view(),name='sign-in'),
path('Logout', views.handelLogout, name="handleLogout"),
# path('cu_add/', views.cu_add, name="cu_add"),
path('xyz_a', views.yz_a, name="xyz_a"),
# path('view_c/', views.view_cu, name="view_cu"),
# path('delete_member(?p<int:pid>)', Delete_Member, name='delete_member'),
# path('Accept_member(?p<int:pid>)', Accept_Member, name='Accept_member'),

# ytfyuihiojjop
path('ucontact/',Contact, name = 'contact'),
path('uabout/',About, name = 'about'),
# path('sendplan/', views.sendplan, name="sendplan"),
path('myplan/',myplan,name = 'myplan'),

path('myplan/sendplanadmin/', sendplanadmin, name="sendplanadmin"),
path('myplan/viewplan/',viewplan, name="viewplan"),



]