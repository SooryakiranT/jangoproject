from django import forms
from .models import Table1

class Table1Form(forms.ModelForm):
    Password=forms.CharField(widget=forms.PasswordInput,max_length=8,min_length=2)
    Confirmpassword=forms.CharField(widget=forms.PasswordInput,max_length=8,min_length=2)
    class Meta():
        model=Table1
        fields=('Name','Age','Place','Email','Password','Photo')
        label={
            'Name':'',
            'Age': '',
            'Place':'',
            'Email':'',
            'Password':'',
            'Photo':'' ,
             }

class LoginForm(forms.ModelForm):
    Password=forms.CharField(widget=forms.PasswordInput,max_length=8,min_length=6)
    class Meta():
        model=Table1
        fields=('Email','Password')

class UpdateForm(forms.ModelForm):
    Password=forms.CharField(widget=forms.PasswordInput,max_length=8,min_length=2)
    Confirmpassword=forms.CharField(widget=forms.PasswordInput,max_length=8,min_length=2)
    class Meta():
        model=Table1
        fields=('Name','Age','Place','Email','Password','Photo')
        label={
            'Name':'',
            'Age': '',
            'Place':'',
            'Email':'',
            'Password':'',
            'Photo':'' ,
             }
    