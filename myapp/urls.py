from django.contrib import admin
from django.urls import path

from .views import index, acrticles, archive, users

urlpatterns = [
    path('', index, name='index'),
    path('acrticles/', acrticles, name='acrticles'),
    path('acrticles/archive/', archive, name='archive'),
    path('users', users, name='users'),
    path('article/<int:article_number>/archive', users, name='users'),
    path('article/<int:article_number>/<slug:slug_text>', users, name='users'),
    path('users/<int:user_number', users, name='users'),

]
