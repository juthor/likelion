from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from django.utils import timezone
from .forms import BlogPost
# Create your views here.

def home(request):
    blogs=Blog.objects
    return render(request, 'home.html', {'blogs':blogs})


def detail(request, blog_id):
    details=get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'details':details})

def new(request):
    return render(request, 'new.html')

def create(request):
    blog=Blog()
    blog.title=request.POST['title']
    blog.body=request.POST['body']
    blog.pub_date=timezone.datetime.now()
    blog.save()
    return redirect('/blog/'+str(blog.id))

def delete(request, blog_id):
    delete_blog=get_object_or_404(Blog, pk=blog_id)
    delete_blog.delete()

    return redirect('home')

def update(request, blog_id):
    update_blog=get_object_or_404(Blog, pk=blog_id)
    return render(request, 'update.html', {'update_blog':update_blog})


def edit(request, blog_id):
    edit_blog=Blog.objects.get(pk=blog_id)
    edit_blog.title=request.POST['title']
    edit_blog.body=request.POST['body']
    edit_blog_pup_date=timezone.datetime.now()
    edit_blog.save()

    return redirect('/blog/'+str(edit_blog.id))
    

def blogpost(request):
    if request.method=="POST":
        form=BlogPost(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.pub_date=timezone.now()
            post.save()
            return redirect('home')

    else: #get 방식으로 들어온 것
        form=BlogPost()
        return render(request, 'new.html', {'form':form})