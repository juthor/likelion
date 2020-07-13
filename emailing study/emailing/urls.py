from django.contrib import admin
from django.urls import path, include
import backapp.views

urlpatterns = [
   path('admin/', admin.site.urls),
   path('', backapp.views.home, name="home"),
   path('mailer/', include('mailer.urls')),
]