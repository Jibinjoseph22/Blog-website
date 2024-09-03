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
    path('edit_blog/<int:blog_id>/', views.edit_blog, name='edit_blog'),  # Edit blog with ID
    path('edit_blog/', views.edit_blog, name='edit_blog'),  # Edit blog without ID
    path('blog_list/', views.blog_list, name='blog_list'),
    path('delete/<int:blog_id>/', views.delete_blog, name='delete_blog'),
    path('main/', views.main_view, name='main'),
    path('blogs/category/<str:category_name>/', views.category_blogs, name='category_blogs'),
    path('main_content/', views.main_content, name='main_content'),


]
