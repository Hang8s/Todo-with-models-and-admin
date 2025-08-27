from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Task

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2']
        
class AddForm (ModelForm):
    class Meta:
        model = Task
        fields = ['title','description','due_date','priority']
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Enter title'}),
            'description': forms.Textarea(attrs={'class': 'input-field', 'placeholder': 'Enter description', 'rows': 3}),
            'is_completed': forms.CheckboxInput(attrs={'class': 'checkbox'}),
        }