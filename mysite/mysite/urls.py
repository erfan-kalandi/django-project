"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from poem import views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.post, name='post'),

    path('poemlist/', views.poemlist, name='poemlist'),

    path('showtext/', views.showtext, name='showtext'),

    path('searchword/', views.searchword, name='search'),

    path('searchstartword/', views.searchstartword, name='search'),

    path('poetlist/', views.poetlist, name='poetlist'),

    path('create/', views.create, name='create'),

    path('poetlist/<int:id>/', views.poemlist, name='poemlist')

]
