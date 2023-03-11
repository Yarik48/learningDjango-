from cProfile import label

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db.models import Model
from django.forms import ModelForm, TextInput, Select, DateInput, FileInput, Textarea
from django.http import request

from .models import *


class AddPostForm(ModelForm):
    day = forms.ModelChoiceField(queryset=Day.objects.all(), empty_label="День недели", widget=forms.Select(attrs={'class':'form-control'}))
    object = forms.ModelChoiceField(queryset=Object.objects.all(), empty_label="Предмет", widget=forms.Select(attrs={'class':'form-control'}))

    class Meta:
        model = Posts
        fields = ['text','day','object','date','file']

        widgets = {
            'text': Textarea(attrs={'class':'form-control', 'label':'Задание'}),
            'day': Select(attrs={'class': 'form-control', 'empty_label':'Предмет'}),
            'object': Select(attrs={'class':"form-control"}),
            'date': DateInput(attrs={'class': 'form-control','type':'date'}),
            'file': FileInput(attrs={'class': 'form-control', 'placeholder':'Прикрепите файл'})
        }


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(max_length=100, label="Имя пользователя",widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'miНейм'}))
    password1 = forms.CharField(max_length=100, label="Пароль", widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Пароль'}))
    password2 = forms.CharField(max_length=100, label="Повтор", widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Повтор пароля'}))

    class Meta:
        model = User
        fields = ('username','password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(max_length=100, label='',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ваше имя'}))
    password = forms.CharField(max_length=100, label='' ,widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль'}))


    class Meta:
        model = User
        fields = ('username','password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }


class AddMessageForm(ModelForm):
    class Meta:
        model = Messages
        fields = ['author', 'text']
