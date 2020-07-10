from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User

from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.core.mail import EmailMessage
from .tokens import account_activation_token
from django.utils.encoding import force_bytes, force_text

# Create your views here.

def signup(request):
    if request.method == "POST":
        if request.POST["password1"] == request.POST["password2"]:
            user = User.objects.create_user(username=request.POST["username"], email=request.POST["email"], password=request.POST["password1"])
            
            user.is_active=False
            user.save()
            current_site=get_current_site(request)
            message=render_to_string('activation_email.html', {
                'user':user,
                'domain':current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)), #.decode를 지우기
                'token':account_activation_token.make_token(user),
            })
            mail_title="계정 활성화 확인 이메일"
            mail_to=request.POST["email"]
            email=EmailMessage(mail_title, message, to=[mail_to])
            email.send()            

            return redirect("home")
    return render(request, 'signup.html')

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error' : "username or password is invalid"})
    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')

def activate(request, uidb64,token):
    try:
        uid=force_text(urlsafe_base64_decode(uidb64))
        user=User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user=None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_activate=True
        user.save()
        auth.login(request, user)
        return redirect("home")
    else:
        return render(request, 'home.html', {'error':'계정 활성화 오류'})