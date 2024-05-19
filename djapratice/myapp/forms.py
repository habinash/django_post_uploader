from django import forms

class PostForm(forms.Form):
    text=forms.CharField()
    matter=forms.CharField()
    image=forms.FileField()