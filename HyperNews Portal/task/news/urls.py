"""hypernews URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from . import views

urlpatterns = [
    path('', views.Index.as_view()),
    #path('news/<int:post_id>/', views.Article.as_view(), name='article'),
    path('news/', views.news_list),
    path('news/<int:post_id>/', views.article, name='article'),
    path('news/create/', views.CreateArticle.as_view(), name='create'),
    #path('news/?q', views.qu),
]
