from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('search', views.search, name='search'),
    path('posts', views.post_list, name='post_list'),
    path('cat/dr', views.cat_dr, name='post_list'),
    path('cat/na', views.cat_na, name='post_list'),
    path('cat/th', views.cat_th, name='post_list'),
    path('cat/pe', views.cat_pe, name='post_list'),
    path('cat/sc', views.cat_sc, name='post_list'),
    path('cat', views.cat, name='categories'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]
