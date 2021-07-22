from django import forms
from django.http import request
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordChangeForm



# Sign Up Form
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    email = forms.EmailField(max_length=200, help_text='Enter a valid email address')

    class Meta:
        model = User
        fields = [
            'username', 
            'first_name', 
            'last_name', 
            'email', 
            'password1', 
            'password2', 
            ]

class LoginUserForm(AuthenticationForm):
    username=forms.CharField(max_length=30,required=True)
    # password=forms.CharField(widget=forms.PasswordInput,max_length=30,required=True) #NOTE:Include this is you want some other field cutomization accept basic
    class Meta:
        model = User
        fields = [
            'username',
            # 'password',
            
        ]

class ChangePasswordForm(PasswordChangeForm):
    class Meta:
        model=User


class EditUserProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude=['user']
        
           
            
        