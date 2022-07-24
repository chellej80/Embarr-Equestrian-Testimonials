from django import forms
from .models import Comment, UserProfile
from django.contrib.auth.models import User


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('rating', 'name', 'location', 'body')


class UserUpdateForm(forms.ModelForm):
    """
    Form for profile name update
    """
    email = forms.EmailField()
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'bio']


class searchForm(forms.Form):
    q = forms.CharField()
