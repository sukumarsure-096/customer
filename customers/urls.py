"""customers URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('c',c,name='c'),
    path('f',f,name='f'),
    path('az',az,name='az'),
    path('cus',cus,name='cus'),
    path('fc',fc,name='fc'),
    path('ff',ff,name='ff'),
    path('fa',fa,name='fa'),
    path('fcus',fcus,name='fcus'),
    path('log',log,name='log')
]
