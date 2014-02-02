from django.shortcuts import render
from django.http import HttpResponse
from models import Blog

# Create your views here.

def test_view(request):
	return HttpResponse("Hello World")

def test_view2(request):
	user_ip = request.META["REMOTE_ADDR"]
	response_var = "User IP: %s" %(user_ip) 
	return HttpResponse(response_var)

def list_blogs(request):
	blogs = Blog.objects.all()
	return render(request,"list_blogs.html")
