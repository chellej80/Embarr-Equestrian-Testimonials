from django import forms
from django.contrib.auth.models import User
from .models import Review


class ReviewForm(forms.ModelForm):
    """
    Submit Form for the Reviews
    """
    class Meta:
        model = Review
        fields = ('rating', 'location', 'body')


class UserUpdateForm(forms.ModelForm):
    """
    Form for profile update
    """
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
