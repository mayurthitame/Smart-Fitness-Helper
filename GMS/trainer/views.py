from django.shortcuts import render,redirect, HttpResponse
from django.views import View
from .forms import SignUpForm,MySignInForm
from gym.models import  trainer_MC
from core.models import xyz_a
from .models import TProfile, sendPlan
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
import uuid
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

from .models import *
from .models import Bmi
class Home(View):
    def get(self,request):
        return render(request,'trainer/home.html')
class customerplan(View):
    def get(self,request):
        return render(request,'trainer/c_plan.html')
# class sendplan(View):
#     def get(self,request):
#         return render(request,'trainer/sendplan.html')


def Tsend_email_after_registration(email,token):
    
    subject="Verify Email"
    message=f' Hi Your_usern:-  Click on the link to verify  your account http://127.0.0.1:8000/Taccount-verify/{token}'
    from_email=settings.EMAIL_HOST_USER
    recipient_list=[email]
    send_mail(subject=subject,message=message,from_email=from_email,recipient_list=recipient_list)
class SignUpView(View):
    def get(self,request):
        fm=SignUpForm()
        return render(request,'trainer/sign-up.html',{'form':fm})
    def post(self,request):
        fm=SignUpForm(request.POST)
       
        if fm.is_valid():
          
            new_user=fm.save()
            uid=uuid.uuid4()
            pro_obj=TProfile(user=new_user,token=uid)
            pro_obj.save()
            Tsend_email_after_registration(new_user.email,uid)
            messages.info(request,"Your account is not verifyed,please check Your EMAIL ,and verify your ACCOUNT")
            return redirect('/Tsign-up/')
        
        else:
            messages.error(request,"Invalid credentials! Please try again")
            return render(request, 'trainer/home.html') 
def Taccount_verify(request,token):
    pf=TProfile.objects.filter(token=token).first()
    pf.verify=True
    pf.save()
    
    messages.success(request ,"Your account has been verified , Now you can login ")
    return redirect('/Tsign-in')


class SignInView(View):
    def get (self,request):
        fm=MySignInForm()
        return render(request,'trainer/sign-in.html',{'form':fm})
    def post(self,request):
        fm=MySignInForm(request,data=request.POST)
        if fm.is_valid():
            username=fm.cleaned_data['username']
            password=fm.cleaned_data['password']
            user=authenticate(username=username,password=password)
            if user is not None:
                pro=TProfile.objects.get(user=user)
                if pro.verify:
                    login(request,user)
                    messages.success(request, "Successfully Logged In")
                    return redirect('/Thome')
                else:
                    messages.info(request,"Your account is not verifyed"
                    )
                    return redirect('/Tsign-in')
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("/Tsign-in")

        # return HttpResponse("404- Not found")
            # pro=Profile.objects.get(user=user)
            # if pro.verify:

            #    login(request,user)
            #    return redirect('/')
               
            # else:
               
            #     messages.info(request,"Your account is not verifyed,please check Your EMAIL ,and verify your ACCOUNT"
            #     )
            #     return redirect('/sign-in')
# Create your views here.
def handelLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('/Thome')

# esrdtyugiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiioooooooooooooooooooooooo
def BMIC(request):
    context = {}
    if request.method=="POST":
        weight_metric = request.POST.get("weight-metric")
        weight_imperial = request.POST.get("weight-imperial")

        if weight_metric:
            weight = float(request.POST.get("weight-metric"))
            height = float(request.POST.get("height-metric"))
           
            age= request.POST.get("age-metric")

        elif weight_imperial:
          
            age= request.POST.get("age-imperial")


            weight = float(request.POST.get("weight-imperial"))/2.205
            height = (float(request.POST.get("feet"))*30.48 + float(request.POST.get("inches"))*2.54)/100

        bmi = (weight/(height**2))
        save = request.POST.get("save")
        if save == "on":
            Bmi.objects.create(weight=weight, age=age, height=height, bmi=round(bmi))
        if bmi < 16:
            state = "Severe Thinness"
        elif bmi > 16 and bmi < 17:
            state = "Moderate Thinness"
        elif bmi > 17 and bmi < 18:
            state = "Mild Thinness"
        elif bmi > 18 and bmi < 25:
            state = "Normal"
            # context["bmi"] = round(bmi)
            # context["state"] = state
       
            # return redirect("/normal",context)

        elif bmi > 25 and bmi < 30:
            state = "Overweight"
        elif bmi > 30 and bmi < 35:
            state = "Obese Class I"
        elif bmi > 35 and bmi < 40:
            state = "Obese Class II"
        elif bmi > 40:
            state = "Obese Class III"
      
        context["bmi"] = round(bmi)
        context["state"] = state
       
    return render(request,"trainer/BMIC.html",context)
    
def normal(request): 
  
        
    return render(request,"trainer/normal.html")
def view_trainer(request):
    
    if request.method=="POST":
        traineri= request.POST.get('traineri')
        customeri = request.POST.get('customeri')
      
        Trainer_I=trainer_MC(  traineri= request.POST.get('traineri'),
        customeri = request.POST.get('customeri'),
      
         )
        

       
         # m=R_team.objects.values_list('birthday', flat=True).latest('birthday')
       
       
        
       
        
         
        
        if  traineri==''or  customeri=='' :
            messages.error(request,"please fill the form correctly")
       
        
         # else:
         #     Xyz_a= xyz_a.objects.create(name=name, emailid=emailid, contact=contact,age=age,gender=gender,weight=weight)
         #     Xyz_a.save()
         #     messages.success(request, 'your message has been sent!')
        else:
            Trainer_I=trainer_MC.objects.create( traineri= traineri,customeri=customeri)
            # Trainer_I=trainer_MC.save()
            messages.success(request, "Successfully send data")
            return redirect('/Home')
    member = TProfile.objects.all()
    d = {'member': member}
        # return redirect('view_trainer/',d)
        
    return render(request, 'view_trainer.html',d)




def view_trainermanageC(request):
    member = trainer_MC.objects.all()
    d = {'member': member}

        # return redirect('view_trainer/',d)
        
    return render(request, 'trainer/view_trainermanagec.html',d)

def search (request):
    query=request.GET['query']
    if not query or query == "":
        messages.error(request, "Please put input")
        return redirect("/Thome")
    if len(query)>78:
       img=xyz_a.objects.none()
    else:
        img=xyz_a.objects.filter( id__icontains=query)
       
    if img.count()==0:
        pass
    params={'img': img, 'query': query}
    return render(request, 'trainer/search.html', params)
# def sendplan(request):
#     error = ""
#     if request.method == 'POST':
#         name1= request.POST.get['name1']
#         amount= request.POST.get['amount']
#         duration = request.POST.get['duration']
#         planN = request.POST.get['planN']
#         Xyz_a=sendPlan(  name= request.POST.get['name'],
#         amount= request.POST.get['amount'],
#         duration = request.POST.get['duration'],
#         planN = request.POST.get['planN'],
#         )
      
#         try:
#             Xyz_a=sendPlan.objects.create( name1=name1, amount=amount, duration=duration, planN= planN)
#             Xyz_a=sendPlan.save()
#             error = "no"
#         except:
#             error = "yes"
#     d = {'error': error}
#     return render(request, 'trainer/sendplan.html', d)
def sendplan(request):
    
    if request.method == 'POST':
        name1= request.POST.get('name1'),
        amount= request.POST.get('amount')
        duration = request.POST.get('duration')
        planN = request.POST.get('planN')
        Xyz_a=sendPlan(  name1= request.POST.get('name1'),
        amount= request.POST.get('amount'),
        duration = request.POST.get('duration'),
        planN = request.POST.get('planN'),
        )
      
       
        
        sendPlan.objects.create( name1=name1, amount=amount, duration=duration, planN= planN)
        messages.success(request, "Successfully send")
  
    #         error = "no"
    #     except:
    #         error = "yes"
    # d = {'error': error}
    return render(request, 'trainer/sendplan.html')
