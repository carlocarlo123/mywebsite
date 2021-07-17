from django.shortcuts import render  
from django.core.mail import send_mail

# Create your views here.
def home(request):
	return render(request,'home.html',{})


def contact(request):
	if request.method== "POST":
		message_name=request.POST['message-name']
		message_email=request.POST['message-email']
		message=request.POST['message'] 

		#send email 
		send_mail(message_name, message, message_email, ['carloab39@gmail.com'])

		return render(request,'contact.html',{'message_name':message_name})## 
	else:
		return render(request,'contact.html',{})
def about(request):
	return render(request,'about.html',{})

def service(request):
	return render(request,'service.html',{})

def pricing(request):
	return render(request,'pricing.html',{})

def blog(request):
	return render(request,'blog.html',{})

def blog_details(request):
	if request.method=="POST":
		search=request.POST['search']
		return render(request,'https://www.google.com',{'search':search})
	else:

		return render(request,'blog_details.html',{})