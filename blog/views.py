from django.shortcuts import render, redirect
from django.http import HttpResponse
from models import Blog
from datetime import datetime
from django.core.context_processors import csrf

# Create your views here.

def test_view(request):
	return HttpResponse("Hello World")

def test_view2(request):
	user_ip = request.META["REMOTE_ADDR"]
	response_var = "User IP: %s" %(user_ip) 
	return HttpResponse(response_var)

def list_blogs(request):
	blog_list = Blog.objects.all()
	return render(request,"list_blogs.html",{'blogs':blog_list})

def new_blog(request):
	if request.method != 'POST':
		c = {}
		c.update(csrf(request))
		return render(request, "new_blog_form.html",c)
	else:
		blog = Blog(baslik=request.POST['baslik'],icerik=request.POST['icerik'],olusturulma_tarihi=datetime.today())
		blog.save()
		return redirect('/blog/list_blogs')

def edit_blog(request,blog_id):
	if request.method != 'POST':
		b = Blog.objects.get(id=blog_id)
		c = {'blog':b}
		c.update(csrf(request))
		return render(request, "edit_blog_form.html",c)		
	else:
		b = Blog.objects.get(id=blog_id)
		b.baslik = request.POST['baslik']
		b.icerik = request.POST['icerik']
		b.save()
		return redirect('/blog/list_blogs')
