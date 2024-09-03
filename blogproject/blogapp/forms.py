from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Blog

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=False, max_length=10)

    class Meta:
        model = User
        fields = ('username', 'email', 'phone_number', 'password1', 'password2')

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if phone_number:
            if not phone_number.isdigit() or len(phone_number) != 10:
                raise forms.ValidationError('Phone number must be 10 digits long and contain only numbers.')
        return phone_number

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.phone_number = self.cleaned_data['phone_number']
        if commit:
            user.save()
        return user

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content', 'status', 'category']  # Include the category field
        widgets = {
            'content': forms.HiddenInput(),  # Set content from JavaScript
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Customize error messages for required fields
        self.fields['title'].error_messages = {'required': 'Please enter a title for your blog.'}
        self.fields['content'].error_messages = {'required': 'Blog content cannot be empty.'}
        self.fields['category'].error_messages = {'required': 'Please select a category.'}