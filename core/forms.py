from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Category, Article, Comment


class ArticleForm(forms.ModelForm):
    class Meta:
        model =Article
        fields = ['title', 'short_description', 'full_description', 'image', 'category']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'short_description:': forms.Textarea(attrs={
                'class': 'form-control'
            }),
            'full_description:': forms.Textarea(attrs={
                'class': 'form-control'
            }),
            'image:': forms.FileInput(attrs={
                'class': 'form-control'
            }),
            'category:': forms.Select(attrs={
                'class': 'form-select'
            })
            }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'form-control'
            })
        }

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Input your username'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Input your password'
    }))
    class Meta:
        model = User


class RegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Input your username'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Input your password'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Confirm your password'
    }))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your email'
            })
        }