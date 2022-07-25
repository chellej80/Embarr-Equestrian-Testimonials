from django import forms
from .models import Review, UserProfile
from django.contrib.auth.models import User


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('rating', 'location', 'body')


class UserUpdateForm(forms.ModelForm):
    """
    Form for profile name update
    """
    email = forms.EmailField()
    

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class searchForm(forms.Form):
    q = forms.CharField()
