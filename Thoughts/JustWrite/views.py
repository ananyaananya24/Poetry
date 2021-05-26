from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login,logout,authenticate
from .models import add_blog, user_profile
from datetime import datetime

def home(request):
    return render(request, "home.html")


def validation(email, pswd, cpswd):
    
    if '@' not in email:

        return (False, 'Validation Error')

    return (True, 'Validation Ok')



def signup(request):
    if request.method=="POST":
        uname= request.POST.get('uname')
        fname= request.POST.get('fname')
        lname= request.POST.get('lname')
        email= request.POST.get('email')
        pswd= request.POST.get('pswd')
        cpswd= request.POST.get('cpswd')
        print(f"uname {uname}, fname {fname}, lname {lname}, email {email}")

        # val= True
        # if ('@' not in email):
        #     print(f'email {email}')
        #     val= False
        # if pswd != cpswd:
        #     print(f'pswd {pswd}')
        #     val= False
        
        # if val== True:
        #     try:
        #         user = User.objects.get(username = uname)
        #     except:
        #         user = None
        
       
        #     if user is not None:
        #         return HttpResponse(f"{uname}, you are already registered!")
        #     else:
        validate = validation(email, pswd,cpswd)
        if validate[0]:
                reg_user= User(username=uname, first_name=fname, last_name=lname, email=email)
                reg_user.set_password(pswd)
                reg_user.save() 
                prof= user_profile(user=reg_user, address="", mobile_no="", about="") 
                prof.save()          
                return redirect('login')
        else:
            return HttpResponse(validate[1])
    return render(request,'signup.html')



def login(request):
    if request.method=="POST":
        uname= request.POST.get('uname')
        pswd= request.POST.get('pswd')
        user= authenticate(username=uname, password=pswd)
        print(f" {uname}, pswd {pswd}, {user}")
        if user is not None:
            auth_login(request,user)    # Storing user in Session
            return redirect('home')
        else:
            return HttpResponse(f"UserName is Not valid")
    return render(request,'login.html')

def Logout(request):
    logout(request)

    return redirect('home')

def blog(request):
    if request.method=="POST":
        title= request.POST.get('title')
        head= request.POST.get('heading')
        body= request.POST.get('body')
        print(f'title {title}, {body}')
        user= (request.user)         # getting data from session
        blog= add_blog(author=user, title=title, body=body, heading=head)
        blog.save()
        return redirect('home')
    return render(request,"blog.html")

def about(request):
    return render(request,"about.html")

def edit(request):
    if request.method =="POST":

        image = request.FILES['image']      #-----------------for getting image / files from form 
        fname= request.POST.get('fname')
        lname= request.POST.get('lname')
        address= request.POST.get('address')
        mob= request.POST.get('mobile')
        email= request.POST.get('email')
        about= request.POST.get('about')
        dob= request.POST.get('dob')
        #dob_obj= datetime.strptime(dob, '%Y-%m-%d')
        user= User.objects.get(username= request.user.username)  # To edit data in User table
        user.first_name= fname
        user.last_name = lname
        user.email= email
        user.save()
        profile= user_profile.objects.get(user= request.user.id) # foreign key or any relational table get id
        profile.address= address
        profile.mobile_no=mob
        profile.image=image
        profile.about=about
        profile.dob= dob
        #print(type(dob_obj))
        profile.save()
        print(user)
        print(f"fname: {fname}, {lname}, {address}, {mob}, {email}, {dob}")
    prof_data= user_profile.objects.get(user= request.user.id)
    print(prof_data)
    return render(request,"edit_prof.html",{"prof_data":prof_data})

def profile(request):

    if request.method =="POST":

        image = request.FILES['image']      #-----------------for getting image / files from form 
        fname= request.POST.get('fname')
        lname= request.POST.get('lname')
        address= request.POST.get('address')
        mob= request.POST.get('mobile')
        email= request.POST.get('email')
        about= request.POST.get('about')
        dob= request.POST.get('dob')
        #dob_obj= datetime.strptime(dob, '%Y-%m-%d')
    
    prof_data= user_profile.objects.get(user= request.user.id)
    print(prof_data)
    return render(request,"prof.html",{"prof_data":prof_data})

def poem(request):
    return render(request, "poem.html")

def fblog(request):
    return render(request, "frontblog.html")




# Create your views here.



