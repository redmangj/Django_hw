
from django.urls import include, path

from myapp.views import (index, acrticles, archive, users, article_number, article_number_slug, user_number, phone_number,
                         interest)


urlpatterns = [
    path('', index, name='index'),
    path('acrticles/', acrticles, name='acrticles'),
    path('acrticles/archive/', archive, name='archive'),
    path('users/', users, name='users'),
    path('article/<int:article_number>/archive/', article_number, name='article_number'),
    path('article/<int:article_number>/<slug:slug_text>/', article_number_slug, name='article_number_slug'),
    path('users/<int:user_number>/', user_number, name='user_number'),
    path('phone_number/0<int:code_id>/<int:number>', phone_number, name ='phone_number'),
    path('<four_numbers>-<six_numbers>/', interest, name='interest')
]
