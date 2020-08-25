from django.shortcuts import render,HttpResponse,redirect
from datetime import datetime
from mywebsiteapp.models import Contact
from django.contrib import messages

def index(request):
    return render(request,"index.html") 
   
def about(request):
    return render(request,"about.html") 

def projects(request):
    return render(request,"projects.html") 

def resume(request):
    return render(request,"resume.html") 

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        contact = Contact(name=name,email=email,subject=subject,message=message)
        contact.save()
        messages.success(request, 'Your message has been sent')


    return render(request,"contact.html") 


# def view_contact(request):
#     if request.method == "POST":
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         subject = request.POST.get('subject')
#         message = request.POST.get('message')

#         contact = Contact(name=name,email=email,subject=subject,message=message)
#         contact.save()
#         messages.success(request, 'Your message has been sent')
        

#     return render(request,"view_contact.html",{"contact":contact}) 



    

 
 