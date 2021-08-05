from django.http import request
from django.shortcuts import redirect, render

from .form import SignUpForm,VideoForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as auth_login
from django.contrib import messages
from django.core.mail import EmailMessage
from .models import Subject, Youtube

# Create your views here.

#post
#get 
def get_subject(request):
    display = Subject.objects.all()
    return render(request,'home.html',{"list" :display})


def add_subject(request):
    if request.method == "POST":
    
        sname  = request.POST['sname']
        description = request.POST['description']
        if sname != "" and description != "":
            Subject.objects.create(subject_name = sname,description=description )
            return redirect('index')
    return render(request,'add_subject.html')

def delete_subject(request,id):
    sub = Subject.objects.get(id = id)
    sub.delete()
    return redirect('index')



def signup(request):
    form_data = SignUpForm(request.POST)
    print(request.POST)
    if form_data.is_valid():
        form_data.save()
        return redirect('login_page')
    else:
        form_data = SignUpForm()

    return render(request,'signup.html', {'form':form_data})


def upload_video(request):
    video_form = VideoForm()
    if request.method == 'POST':
        video_form = VideoForm(request.POST)
        if video_form.is_valid():
            video_form.save()
            return redirect("see_video")
    return render(request,'video_upload.html', {'form':video_form})

def see_video(request):
    video = Youtube.objects.all()
    print("video-----",video)
    return render(request,"see_video.html",{'video':video})



# def login(request):
    # if request.method == 'POST':
    #     form = AuthenticationForm(request,data=request.POST)
    #     if form.is_valid():
    #         username = form.cleaned_data.get("username")
    #         password = form.cleaned_data.get("password")

    #         user = authenticate(username = username,password = password)
    #         if user is not None:
    #             auth_login(request ,user)
    #             return redirect('bio_page')
    #         else:
    #             messages.error(request,"invalid Username or password")
    #     else:
    #         messages.error(request,"invalid Username or password")
    # else:
    #     form = AuthenticationForm()

    # return render(request,'login.html', {'form':form}) 

def login(request):
    if request.method == 'POST':
        username  = request.POST['username']
        password = request.POST['password']
        
        

        user = authenticate(username = username,password = password)
        if user is not None:
            auth_login(request ,user)
            return redirect('bio_page')
        else:
            messages.error(request,"invalid Username or password")
        


    return render(request,'login.html') 

def logout_request(request):
    logout(request)
    return redirect('login_page')


def contact_us(request):
    if request.method == 'POST':
        name = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        comment = request.POST['comment']

        if email != '':
            info = "name :" + name + " last name : " + lname + " email : " + email + " comment : " + comment 
            email_for_us = EmailMessage("Contact from website", info, to =["nihalhub29@gmail.com"])
            email_for_coustomer = EmailMessage("Email from Niahl website" , "Thank you for contact me", to =[email])
            email_for_coustomer.send()
            email_for_us.send()
            return redirect('bio_page')

    return render(request,'contact.html')

             


    
