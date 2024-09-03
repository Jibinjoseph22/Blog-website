from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import RegistrationForm
from .models import Blog
from .forms import BlogForm


def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful. You can now log in.')
            return redirect('login')
        else:
            messages.error(request, 'Registration failed. Please try again.')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('main_page')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def main_page(request):
    context = {
        'username': request.user.username  # Assuming 'username' is the attribute holding the username
    }
    return render(request, 'main.html', context)

def user_logout(request):
    logout(request)
    return redirect('home')

# views.py
from django.shortcuts import render, redirect
from .models import Blog
from .forms import BlogForm

def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
                # Save as a published blog
                blog = form.save(commit=False)
                blog.author = request.user
                blog.save()
                return redirect('blog_list')  # Redirect to blog list view
    else:
        form = BlogForm()

    return render(request, 'create_blog.html', {'form': form})

def blog_list(request):
    blogs = Blog.objects.filter(author=request.user)
    return render(request, 'blog_list.html', {'blogs': blogs})

def read_blog(request):
    return render(request, 'read_blog.html')

def edit_blog(request):
    return render(request, 'edit_blog.html')

def edit_blog(request, blog_id=None):
    if blog_id:
        blog = get_object_or_404(Blog, id=blog_id)
    else:
        blog = None

    if request.method == 'POST':
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
    else:
        form = BlogForm(instance=blog)

    return render(request, 'edit_blog.html', {'form': form})


def delete_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    if request.method == 'POST':
        blog.delete()
        return redirect('blog_list')
    return render(request, 'confirm_delete.html', {'blog': blog})

def main_view(request):
    return render(request, 'main.html')

def category_blogs(request, category_name):
    blogs = Blog.objects.filter(category__iexact=category_name)
    return render(request, 'category_blogs.html', {'blogs': blogs})

def main_content(request):
    return render(request, 'main_content.html')