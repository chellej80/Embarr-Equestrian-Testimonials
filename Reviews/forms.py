from django import forms
from .models import Comment, UserProfile
from django.contrib.auth.models import User


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('rating','name','location','body')

class searchForm(forms.Form):
    q = forms.CharField()

class UserUpdateForm(forms.ModelForm):
    """
    Form for profile name update
    """
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','first_name', 'last_name']

