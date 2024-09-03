# models.py
from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    STATUS_CHOICES = [
        ('publish', 'Publish'),
    ]
    CATEGORY_CHOICES = [
        ('technology', 'Technology'),
        ('literacy', 'Literacy'),
        ('travel', 'Travel'),
        ('food', 'Food'),
        ('personal', 'Personal'),
        ('business', 'Business'),
        ('education', 'Education'),
        ('health', 'Health'),
        ('fashion', 'Fashion'),
        ('sports', 'Sports'),
        ('artistic', 'Artistic'),
        ('Other', 'Other'),
    ]

    title = models.CharField(max_length=200)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='publish')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='Other')
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
