from django import forms
from .models import Blog
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Création de formulaire Article
class BlogForms(forms.ModelForm):
    # title = forms.CharField()
    # description = forms.CharField()
    # image = forms.ImageField()

    class Meta:
        model = Blog
        fields = ('title', 'image', 'description')


# Création de formulaire de création de compte User
class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'password1',
            'password2',
        ]

""" class RowBlogForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField()
    image = forms.ImageField() 
"""
