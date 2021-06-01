from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('search', views.search, name='search'),
    path('posts', views.post_list, name='post_list'),
    path('categories', views.categories, name='categories'),
    path('categories/<int:pk>', views.categories_detail, name="categories_detail"),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<slug:slug>/', views.test_slug, name='test_slug')
]
