from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import get_user_model #best way instead of "from django.auth import User"

from .models import Hadith, Profile

User = get_user_model() #best way to get User model specifically.

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(
        widget=forms.PasswordInput(  #this line to keep password hidden when typing. 
            attrs={
                'class': 'form-control',
                'id':'user-password'
            }
        )
    )

    #this to validate username and passowrd. 
    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

    #this to validate username
    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username__iexact=username) #iexact to have exact match but not case-sensitive.  
        if not qs.exists():
            raise forms.ValidationError('Invalid User!')
        return username



class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

class HadithForm(ModelForm):
    class Meta:
        model = Hadith
        fields = '__all__'

    #method to put a condition for data restriction
    #clean_nameofthearribute (in model)
    def clean_title(self):
        data = self.cleaned_data.get('title')
        if len(data) < 4:
            raise forms.ValidationError('The is not long enough!')
        return data

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name','email', 'username', 'password1', 'password2']