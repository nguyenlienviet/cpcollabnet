"""cpcollabnet URL Configuration

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
from django.urls import path, include
from django.contrib.auth import views as auth_views

from collabs import views

urlpatterns = [
    path(r'', views.home, name='home'),
    path(r'admin/', admin.site.urls),
    path(r'researchers/<int:rid>/', views.researcher, name='researcher'),
    path(r'search/', views.search, name='search'),
    path(r'pub_submit/', views.pub_submit, name='pub_submit'),
    path(r'pub_submissions/', views.pub_submissions, name='pub_submissions'),
    path(r'pub_review/<int:pk>/', views.pub_review, name='pub_review'),
    path(r'accounts/login/',
         auth_views.LoginView.as_view(template_name='registration/login.html'),
         name='login'),
    path(r'accounts/logout/',
         auth_views.LogoutView.as_view(
                template_name='registration/logout.html'),
         name='logout'),
    # path(r'accounts/', include('django.contrib.auth.urls')),
]
