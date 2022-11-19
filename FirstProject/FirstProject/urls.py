"""FirstProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from FirstApp import views
from MultiviewsApp import views as v1
#from App1 import views;
#from App2 import views;
#approach1
from App1.views import f11;
from App2.views import f22;
#approach2
from App1 import views as v11;
from App2 import views as v22;

#Multiple-URLs same View-function;
from FirstApp import views

#default-url
#from django.conf.urls import url;
from django.urls import re_path;

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Welcome/', views.display),
    path('Welcome2/', views.show),
    path('hello/',views.hello),
    path('dtime/',views.senddatetime),
    
    
    #MultiviewsApp as v1;
    path('mrng/',v1.f1),
    path('aftr/',v1.f2),
    path('evng/',v1.f3),
    
    #Single project-Multiple apps;
    #approach1
    path('hello/',f11),
    path('datetime/',f22),
    
    
    #approach2
    path('hello1/',v11.f11),
    path('datetime1/',v22.f22),
    
    #Multiple-URLs same View-function;
    path('firstdemo/',views.demo),
    path('seconddemo/',views.demo),
    path('thirddemo/',views.demo),
    
    
    #default-url-url() or path()
    #path('$',views.homepage),
    #path('.',views.homepage),
    #path('^.*$',views.homepage),
    re_path("^.*$",views.homepage),
    #url(r'$',views.homepage),
    #url(r'^.*$',views.homepage),  #regex-url-pattern
]
