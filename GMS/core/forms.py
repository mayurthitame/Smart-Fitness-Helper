from django import forms
from django.contrib.auth.forms import UserCreationForm,UsernameField,AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import password_validation

from core.models import SignUp
class SignUpForm(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control'}),
       
    )
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control'}),
        strip=False,
        
    )

    email=forms.CharField(label="Email",widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name=forms.CharField(label="First Name",widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name=forms.CharField(label="Last Name",widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
            model = SignUp
            fields = ("username","first_name","last_name","email")
    class Meta:
        model = User
        fields = ("username","first_name","last_name","email")
        
class MySignInForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True,'class':'form-control'}))
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}),
    )

