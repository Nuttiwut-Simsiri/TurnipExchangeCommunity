from django import forms
from django.contrib.auth import authenticate

class SignUpForm(forms.Form):
    firstname = forms.CharField(label="id_firstname")
    lastname = forms.CharField(label="id_lastname")
    username = forms.CharField(label="id_username")
    email = forms.EmailField(label="id_email")
    password = forms.CharField(label="id_password", max_length=50, widget=forms.PasswordInput()) 


class LoginForm(forms.Form):
    username = forms.CharField(label="id_username")
    password = forms.CharField(label="id_password", max_length=50, widget=forms.PasswordInput()) 

    def clean(self, *agrs, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)

            if not user:
                raise forms.ValidationError('We not found this member in our community')
            
            if not user.check_password(password):
                raise forms.ValidationError('Something wrong about your password')
            
            return super(LoginForm, self).clean()