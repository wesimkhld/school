"""advcbv URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from basic_app import views

urlpatterns = [
    url(r'^admin/', admin.site.urls,name='admin'),
    url(r'^$',views.IndexView.as_view()),
    url(r'^basic_app/',include('basic_app.urls',namespace='basic_app')),
    # wisam note: i use namespace for apps so if different apps has same url
    #names no conflict will happen. for example if i have url name ='login'
    #inside this app and inside other apps to call this url in this app we use:
    # reverse('namespace:name') or reverse('basic_app:login') for this example.
    # url(r'^$',views.CBView.as_view()),
    # url(r'^$',views.index)
]
