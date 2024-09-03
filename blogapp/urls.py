from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('main/', views.main_page, name='main_page'),
    path('logout/', views.user_logout, name='logout'),
     path('create/', views.create_blog, name='create_blog'),
    path('read_blog/', views.read_blog, name='read_blog'),
    path('my_blogs/', views.my_blogs, name='my_blogs'),
    path('drafts/', views.drafts, name='drafts'),
     path('blog_list/', views.blog_list, name='blog_list'),
     path('edit_blog/<int:blog_id>/', views.edit_blog, name='edit_blog'), 
     path('delete/<int:blog_id>/', views.delete_blog, name='delete_blog'), 

]
