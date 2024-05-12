from django import forms
from core import models

class CategoryForm(forms.ModelForm):
    class Meta:
        model = models.Category
        fields = ("name",)
    
    name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={
        'placeholder': 'category name',
        'class': 'input'
    }))