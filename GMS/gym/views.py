from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from core.models import xyz_a
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages

from trainer.models import sendPlan

from .models import *
from core.models import SendPlanadmin

# Create your views here.


def Home(request):
    if not request.user.is_staff:
        return redirect('login')
    return render(request, 'index.html')


def About(request):
    return render(request, 'about.html')


def Contact(request):
    return render(request, 'contact.html')


def Login(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['uname']
        p = request.POST['pwd']

        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request, user)
                error = "no"
                # return redirect('Home')
            else:
                error = "yes"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'login.html', d)


def Logout(request):
    if not request.user.is_staff:
        return redirect('login')
    logout(request)
    return redirect('login')


def Add_Enquiry(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    if request.method == 'POST':
        n = request.POST['name']
        c = request.POST['contact']
        e = request.POST['emailid']
        a = request.POST['age']
        g = request.POST['gender']
        try:
            Enquiry.objects.create(
                name=n, contact=c, emailid=e, age=a, gender=g)
            error = "no"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'add_enquiry.html', d)


def View_Enquiry(request):
    enq = Enquiry.objects.all()
    d = {'enq': enq}
    return render(request, 'view_enquiry.html', d)
def Delete_Enquiry(request,pid):
    enquiry = Enquiry.objects.get(id=pid)
    enquiry.delete()
    return redirect('view_enquiry')


def Add_Equipment(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    if request.method == 'POST':
        n = request.POST['name']
        p = request.POST['price']
        u = request.POST['unit']
        d = request.POST['date']
        desc = request.POST['desc']
        try:
            Equipment.objects.create( name=n, price=p, unit=u, date=d, description=desc)
            error = "no"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'add_equipment.html', d)


def View_Equipment(request):
    equ = Equipment.objects.all()
    d = {'equ': equ}
    return render(request, 'view_equipment.html', d)

def Delete_Equipment(request,pid):
    equipment = Equipment.objects.get(id=pid)
    equipment.delete()
    return redirect('view_equipment')

def Add_Plan(request):
    error = ""
    # if not request.user.is_staff:
    #     return redirect('login')
    if request.method == 'POST':
        n = request.POST.get('name')
        a = request.POST.get('amount')
        d = request.POST.get('duration')
        try:
            Plan.objects.create( name=n, amount=a, duration=d)
            error = "no"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'add_plan.html', d)


def View_Plan(request):
    pln = Plan.objects.all()
    d = {'pln': pln}
    return render(request, 'view_plan.html', d)

def Delete_Plan(request,pid):
    plan = Plan.objects.get(id=pid)
    plan.delete()
    return redirect('view_plan')

def Add_Member(request):
    error = ""
    plan1 = Plan.objects.all()
    if not request.user.is_staff:
        return redirect('login')
    if request.method == 'POST':
        n = request.POST['name']
        c = request.POST['contact']
        e = request.POST['emailid']
        a = request.POST['age']
        g = request.POST['gender']
        p = request.POST['plan']
        joindate = request.POST['joindate']
        expiredate = request.POST['expdate']
        initialamount = request.POST['initialamount']
        plan = Plan.objects.filter(name=p).first()
        try:
            Member.objects.create( name=n, contact=c,emailid=e, age=a,gender=g,plan=plan, joindate=joindate, expiredate = expiredate, initialamount = initialamount)
            error = "no"
        except:
            error = "yes"
    d = {'error': error, 'plan':plan1}
    return render(request, 'add_member.html', d)


def View_Member(request):
    member = Member.objects.all()
    d = {'member': member}
    return render(request, 'view_member.html', d)

def Delete_Member(request,pid):
    member = Member.objects.get(id=pid)
    member.delete()
    return redirect('view_member')
def view_cus(request
):
  
    # user = request.user
    
   
    member = xyz_a.objects.all()
    d = {'member': member}
    return render(request, 'view_cus.html', d)
def Delete_Member(request,pid):
        member = xyz_a.objects.get(id=pid)
        send_email_after_(member.emailid)
        member.delete()
       
        return redirect('view_cus')

        
def send_email_after_(emailid):
    
    subject="Ruequest Decline "
    message=f' Hi Your  request is decline '
    from_email=settings.EMAIL_HOST_USER
    recipient_list=[emailid]
    send_mail(subject=subject,message=message,from_email=from_email,recipient_list=recipient_list)
def Accept_Member(request,pid):
        member = xyz_a.objects.get(id=pid)
        send_email_after_A(member.emailid)
       
       
        return redirect('view_cus')
def send_email_after_A(emailid):
    
    subject="Ruequest Accepted "
    message=f' Hi Your  request is Accepted '
    from_email=settings.EMAIL_HOST_USER
    recipient_list=[emailid]
    send_mail(subject=subject,message=message,from_email=from_email,recipient_list=recipient_list)

def trainerMC( request ):
   
    # m=R_team.objects.latest('birthday')
    error = ""
    if request.method=="POST":
        traineri= request.POST.get('traineri')
        customeri = request.POST.get('customeri')
      
        Trainer_I= trainer_MC(  traineri= request.POST.get('traineri'),
        customeri = request.POST.get('customeri'),
      
        )
        

       
        # m=R_team.objects.values_list('birthday', flat=True).latest('birthday')
       
       
        
       
        
         
        
        if  traineri==''or   customeri=='' :
            messages.error(request,"please fill the form correctly")
       
        
        # else:
        #     Xyz_a= xyz_a.objects.create(name=name, emailid=emailid, contact=contact,age=age,gender=gender,weight=weight)
        #     Xyz_a.save()
        #     messages.success(request, 'your message has been sent!')
       
            trainer_MC.objects.create( traineri= traineri, customeri= customeri)
            trainer_MC.save()
            error = "no"
    #     except:
    #         error = "yes"
    # d = {'error': error, }
        # Trainer_manage_C.objects.create(Trainer=Trainer,Customer=Customer)
        # Trainer_manage_C.save()
        # messages.success(request, "Successfully send data")
    return render(request, 'trainer/xyz.html')

def cviewplan(request):
    member = SendPlanadmin.objects.all()
    d = {'member': member}

        # return redirect('view_trainer/',d)
        
    return render(request, 'cviewplan.html',d)
