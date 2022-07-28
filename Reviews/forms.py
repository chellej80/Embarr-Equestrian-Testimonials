"""Forms Imports"""
from django import forms
from django.contrib.auth.models import User
from .models import Review


class ReviewForm(forms.ModelForm):
    """
    Submit Form for the Reviews
    """
    class Meta:
        """Form fields"""
        model = Review
        fields = ('rating', 'location', 'body')


class UserUpdateForm(forms.ModelForm):
    """
    Form class for the user profile update
    """
    email = forms.EmailField()

    class Meta:
        """Form fields"""
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
