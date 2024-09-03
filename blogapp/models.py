# models.py
from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    STATUS_CHOICES = [
        ('published', 'Published'),
        ('draft', 'Draft'),
    ]
    CATEGORY_CHOICES = [
        ('technology', 'Technology'),
        ('literacy', 'Literacy'),
        ('travel', 'Travel'),
        ('food', 'Food'),
        ('personal', 'Personal'),
        ('relations', 'Family/Relations'),
        ('business', 'Business'),
        ('education', 'Education'),
        ('health', 'Health'),
        ('fashion', 'Fashion'),
        ('sports', 'Sports'),
        ('artistic', 'Artistic'),
        ('general', 'Other'),
    ]

    title = models.CharField(max_length=200)
    content = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='general')
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    #draft
class Draft(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.CharField(max_length=20, choices=Blog.CATEGORY_CHOICES, default='general')
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
