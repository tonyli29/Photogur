from django.forms import CharField, PasswordInput, ModelForm
from django import forms
from .models import Picture, Comment

class LoginForm(forms.Form):
    username = CharField(label='User Name', max_length=64)
    password = CharField(widget=PasswordInput())

class PictureForm(ModelForm):

    class Meta:
        model = Picture
        fields = [
            'title',
            'artist',
            'url'
        ]

class CommentForm(ModelForm):

    class Meta:
        model = Comment
        widgets = {
            'picture': forms.HiddenInput(),
            'user': forms.HiddenInput(),
            'name': forms.HiddenInput()
        }
        fields = [
            'name',
            'message',
            'picture',
            'user'
        ]
