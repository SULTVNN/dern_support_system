from django.contrib.auth.forms import AuthenticationForm ,UserModel ,UserCreationForm 
from django.contrib.auth.models import User
from django.forms.models import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from core.models import User , Category
from . import models

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'name', 'user_type', 'password1', 'password2')
    email = forms.EmailField(max_length=254, required=True, widget=forms.EmailInput(attrs={
        'placeholder': 'Your Emial',
        'class': 'input'
    }))
    name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={
        'placeholder': 'Your name',
        'class': 'input'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your Password',
        'class': 'input'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your Password',
        'class': 'input'
    }))
    user_type = forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'radio'}), choices=User.USER_TYPE_CHOICES)


class Login(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Email'
        self.fields['username'].widget.attrs['class'] = 'input'
        self.fields['username'].label = 'Email'
        self.fields['password'].label = 'Password'
        self.fields['password'].widget.attrs['placeholder'] = 'password'
        self.fields['password'].widget.attrs['class'] = 'input'

    username = forms.EmailField(max_length=254, label='', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))

class ProblemForm(forms.ModelForm):
    def __init__(self, *args, user=None, **kwargs):
        super(ProblemForm, self).__init__(*args, **kwargs)
        self.user = user
        self.fields['category'].queryset = Category.objects.all()  # Ensure queryset is refreshed

    class Meta:
        model = models.Orders
        fields = ("problem", "category",)  # Removed 'user' field as it's handled separately
    
    problem = forms.CharField(required=True, widget=forms.Textarea(attrs={
        'placeholder': 'problem ',
    }))
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        empty_label=None,
        required=True,
        widget=forms.Select(attrs={
            'placeholder': 'category',
            'class': 'input'
        })
    )

class CategoryForm(forms.ModelForm):
    class Meta:
        model = models.Category
        fields = ("name",)
    
    name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={
        'placeholder': 'category name',
        'class': 'input'
    }))