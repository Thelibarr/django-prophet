from django import forms
from django.contrib.auth.models import User

class PostForm(forms.Form):
    ticker = forms.CharField(max_length=6)


class UserForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']




