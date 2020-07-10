from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog
	
def home(request):
    blogs = Blog.objects
    return render(request, 'home.html', {'blogs': blogs})

def detail(request, blog_id): 
	details = get_object_or_404(Blog, pk=blog_id)
	return render(request, 'detail.html', {'details':details})

def new(request):
    return render(request, 'new.html')

def create(request):
    blog = Blog()
    blog.title = request.POST['title']
    blog.body = request.POST['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/'+str(blog.id)) 

def delete(request, blog_id):
    destroy = get_object_or_404(Blog, pk=blog_id)
    destroy.delete()
    return redirect('home')

def update(request, blog_id):
    updates= get_object_or_404(Blog, pk=blog_id)
    return render(request, 'update.html', {'updates': updates})

def edit(request, blog_id):
    edit = Blog.objects.get(pk=blog_id)
    edit.title = request.POST['title']
    edit.body = request.POST['body']
    edit.pub_date = timezone.datetime.now()
    edit.save()
    return redirect('home')

#######################################
def rule(request):
    return render(request, 'rule.html')

def contri(request):
    return render(request, 'contri.html')