from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('rating','name','location','body')

class searchForm(forms.Form):
    q = forms.CharField()
