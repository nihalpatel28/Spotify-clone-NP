from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.forms import fields,ModelForm
from .models import Youtube


#username,password,password conformation

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=50,required=True)
    last_name = forms.CharField(max_length=50,required=True)
    email = forms.EmailField(max_length=250,required=False)

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')

class VideoForm(ModelForm):
    class Meta:
        model = Youtube
        fields = "__all__"
