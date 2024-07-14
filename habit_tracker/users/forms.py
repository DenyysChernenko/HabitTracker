from django import forms
from .models import User
from django.forms import ModelForm
from django.core.exceptions import ValidationError


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'profile_picture']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control',
                                               'placeholder': 'Your Username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control',
                                             'placeholder': 'youremail@gmail.com'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control',
                                                   'placeholder': 'At least 8 characters'}),
            'profile_picture': forms.FileInput(attrs={'class': 'form-control'})
        }

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise ValidationError("Password Must be At least 8 Characters")
        return password

    def clean_username(self):
        username = self.cleaned_data['username']
        all_usernames = [user.username for user in User.objects.all()]

        if username in all_usernames:
            raise forms.ValidationError("Username already exists. Please choose a different username.")

        return username
