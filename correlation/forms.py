from django import forms

class PostForm(forms.Form):
    ticker = forms.CharField(max_length=200)



