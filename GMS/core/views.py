from django.shortcuts import render,redirect, HttpResponse
from django.views import View
from .forms import SignUpForm,MySignInForm
from .models import Profile
from trainer.models import sendPlan
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
import uuid
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

from .models import xyz_a,SendPlanadmin

class Home(View):
    def get(self,request):
        return render(request,'core/home.html')
def viewplan(request):
    
        return render(request,'core/c_plan.html')
#
def About(request):
    return render(request, 'core/about.html')


def Contact(request):
    return render(request, 'core/contact.html')

def send_email_after_registration(email,token):
    
    subject="Verify Email"
    message=f' Hi Your_usern:-  Click on the link to verify  your account http://127.0.0.1:8000/account-verify/{token}'
    from_email=settings.EMAIL_HOST_USER
    recipient_list=[email]
    send_mail(subject=subject,message=message,from_email=from_email,recipient_list=recipient_list)
class SignUpView(View):
    def get(self,request):
        fm=SignUpForm()
        return render(request,'core/sign-up.html',{'form':fm})
    def post(self,request):
        fm=SignUpForm(request.POST)
       
        if fm.is_valid():
          
            new_user=fm.save()
            uid=uuid.uuid4()
            pro_obj=Profile(user=new_user,token=uid)
            pro_obj.save()
            send_email_after_registration(new_user.email,uid)
            messages.success(request,"Your Account Created Successfuly, to Verify your Account Check your EMAIL ")
            return redirect('/sign-up/')
        
        else:
            messages.error(request,"Invalid credentials! Please try again")
            return render(request, 'core/home.html') 
def account_verify(request,token):
    pf=Profile.objects.filter(token=token).first()
    pf.verify=True
    pf.save()
    messages.success(request ,"Your account has been verified , Now you can login ")
    return redirect('/sign-in/')


class SignInView(View):
    def get (self,request):
        fm=MySignInForm()
        return render(request,'core/sign-in.html',{'form':fm})
    def post(self,request):
        fm=MySignInForm(request,data=request.POST)
        if fm.is_valid():
            username=fm.cleaned_data['username']
            password=fm.cleaned_data['password']
            user=authenticate(username=username,password=password)
            if user is not None:
                pro=Profile.objects.get(user=user)
                if pro.verify:
                    login(request,user)
                    messages.success(request, "Successfully Logged In")
                    return redirect('/')
                else:
                    messages.info(request,"Your account is not verifyed,please check Your EMAIL ,and verify your ACCOUNT"
                    )
                    return redirect('/sign-in')
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("/sign-in")

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
@login_required(login_url='/sign-in')
def handelLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('/')

# esrdtyugiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiioooooooooooooooooooooooo
  
def normal(request): 
  
        
    return render(request,"core/normal.html")

# def cu_add(request):
#     error = ""
   
#     # if not request.user.verify:
#     #     return redirect('login')
#     if request.method == 'POST':
#         n = request.POST['name']
#         c = request.POST['contact']
#         e = request.POST['emailid']
#         a = request.POST['age']
#         g = request.POST['gender']
#         # p = request.POST['weight']
        
#         try:
#             cu_add.objects.create( name=n, contact=c,emailid=e, age=a,gender=g, )
#             error = "no"
#         except:
#             error = "yes"
#     d = {'error': error, }
#     return render(request, 'core/cu_add.html', d)
@login_required(login_url='/sign-in')
def yz_a( request ):
    error = ""
   
    # m=R_team.objects.latest('birthday')
    
    if request.method=="POST":
        name= request.POST.get('name')
        fname= request.POST.get('fname')
        lname= request.POST.get('lname')
        # contact = request.POST.get('contact')
        emailid= request.POST.get('emailid')
        age= request.POST.get('age')
        gender= request.POST.get('gender')
        weight= request.POST.get('weight')
        height= request.POST.get('height')
        Xyz_a=xyz_a(name= request.POST.get('name'),
        fname= request.POST.get('fname'),
        lname= request.POST.get('lname'),
      
        # contact = request.POST.get('contact'),
       emailid= request.POST.get('emailid'),
       age = request.POST.get('age'),
      gender = request.POST.get('gender'),
        weight= request.POST.get('weight'),
          height= request.POST.get('height'),
        )
        

        # l=xyz_a.objects.all().count()
        # m=R_team.objects.values_list('birthday', flat=True).latest('birthday')
       
       
        
       
        
         
        
        if  emailid=='' or age=='' or name=='' or fname=='' or lname=='' or gender=='' or weight=='' or height=='':
            messages.error(request,"please fill the form correctly")
           
        # elif len((contact))>10:
        #         messages.error(request,"Enter your correct Phone number ")
        
            
        # else:
        #     Xyz_a= xyz_a.objects.create(name=name, emailid=emailid, contact=contact,age=age,gender=gender,weight=weight)
        #     Xyz_a.save()
        #     messages.success(request, 'your message has been sent!')
        try:
            xyz_a.objects.create(name=name,fname=fname,lname=lname, emailid=emailid, age=age,gender=gender,weight=weight ,height=height)
            error = "no"
        except:
            error = "yes"
    d = {'error': error, }
    return render(request, 'core/add.html', d)
# @login_required(login_url='login')
# def view_cu(request
# ):
  
#     # user = request.user
    
   
#     member = xyz_a.objects.all()
#     d = {'member': member}
#     return render(request, 'core/view_cu.html', d)
    # member = xyz_a.objects.filter(user=user)
    # c=xyz_a.objects.all() 
    # return render(request, "core/add.html",{'c':c})
# class Delete_Member(View):

#     def sendmail( request): 
#         user = request.user
#         send_email_after_(user.email)
        
#     def Delete_M(request,pid):
#         member = xyz_a.objects.get(id=pid)
#         member.delete()
#         return redirect('view_cu')
# def Delete_Member(request,pid):
#         member = xyz_a.objects.get(id=pid)
#         send_email_after_(member.emailid)
#         member.delete()
       
#         return redirect('view_cu')

        
# def send_email_after_(emailid):
    
#     subject="Ruequest Decline "
#     message=f' Hi Your  request is decline '
#     from_email=settings.EMAIL_HOST_USER
#     recipient_list=[emailid]
#     send_mail(subject=subject,message=message,from_email=from_email,recipient_list=recipient_list)
# def Accept_Member(request,pid):
#         member = xyz_a.objects.get(id=pid)
#         send_email_after_A(member.emailid)
       
       
#         return redirect('view_cu')
# def send_email_after_A(emailid):
    
#     subject="Ruequest Accepted "
#     message=f' Hi Your  request is Accepted '
#     from_email=settings.EMAIL_HOST_USER
#     recipient_list=[emailid]
#     send_mail(subject=subject,message=message,from_email=from_email,recipient_list=recipient_list)
# def sendplan(request):
#     error = ""
#     if request.method == 'POST':
#         name1= request.POST.get('name1'),
#         amount= request.POST.get('amount')
#         duration = request.POST.get('duration')
#         planN = request.POST.get('planN')
#         Xyz_a=sendPlan(  name1= request.POST.get('name1'),
#         amount= request.POST.get('amount'),
#         duration = request.POST.get('duration'),
#         planN = request.POST.get('planN'),
#         )
      
#         try:
#             Xyz_a=sendPlan.objects.create( name1=name1, amount=amount, duration=duration, planN= planN)
#             Xyz_a=sendPlan.save()
#             error = "no"
#         except:
#             error = "yes"
#     d = {'error': error}
#     return render(request, 'trainer/sendplan.html', d)
def myplan(request):
    user = request.user
    member = sendPlan.objects.filter(name1__icontains=user)
    d = {'member': member}

        # return redirect('view_trainer/',d)
        
    return render(request, 'core/myplan.html',d)
def sendplanadmin(request):
    
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
      
       
        
    
        SendPlanadmin.objects.create( name1=name1, amount=amount, duration=duration, planN= planN)
        messages.success(request, " Ur plan Successfully Registred,You can pay when you come to the GYM and your joining date will start on that day ")
        
    #     error = "no"
    # except:
    #         error = "yes"
    # d = {'error': error}
    user = request.user
    member = sendPlan.objects.filter(name1__icontains=user)
    d = {'member': member}

    return render(request, 'core/sendplanadmin.html',d)
