from django.urls import path
from trainer import views
from . import views
from .views import Home,SignUpView,Taccount_verify,SignInView,customerplan
urlpatterns=[
path('Thome',Home.as_view(),name='Thome'),
path("normal", views.normal, name='normal'),
    
path('Tsign-up/',SignUpView.as_view(),name='Tsign-up'),
path('Taccount-verify/<slug:token>',Taccount_verify,name='Taccount_verify'),
path('Tsign-in/',SignInView.as_view(),name='Tsign-in'),
path('TLogout', views.handelLogout, name="ThandleLogout"),
# path('cu_add/', views.cu_add, name="cu_add"),
# path('xyz_a', views.yz_a, name="xyz_a"),
path('view_trainer/', views.view_trainer, name="view_trainer"),
path('view_trainermanagec/', views.view_trainermanageC, name="view_trainermanagec"),
# path('delete_member(?p<int:pid>)', Delete_Member, name='delete_member'),
# path('Accept_member(?p<int:pid>)', Accept_Member, name='Accept_member'),
# ytfyuihiojjop
path("TBMIC", views.BMIC, name='BMIC'),
path("search/", views.search, name='search'),
path("customerplan/", customerplan.as_view(),name='customerplan'),
# path("sendplan/",sendplan.as_view(),name='sendplan'),
path('sendplan/', views.sendplan, name="sendplan"),

 
 

]