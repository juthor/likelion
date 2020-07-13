from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog

def home(request):
    posts = Blog.objects
    return render(request, 'home.html', {'posts': posts})

def detail(request, post_id):
    post = get_object_or_404(Blog, pk=post_id)
    return render(request, 'detail.html', {'post': post})

def new(request):
    return render(request, 'new.html')

def create(request):
    blog = Blog()
    blog.title = request.POST['name']
    blog.body = request.POST['contents']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/'+str(blog.id))

def delete(request, post_id):
    destroy = get_object_or_404(Blog, pk=post_id)
    destroy.delete()
    return redirect('home')

def update(request, post_id):
    text = get_object_or_404(Blog, pk=post_id)
    return render(request, 'update.html', {'text': text})

def edit(request, post_id):
    edit = Blog.objects.get(pk=post_id)
    edit.title = request.POST['name']
    edit.body = request.POST['contents']
    edit.pub_date = timezone.datetime.now()
    edit.save()
    return redirect('home')