"""Admin Imports"""
from django import forms
from django.contrib import admin
from django.contrib.auth.models import User
from django_summernote.admin import SummernoteModelAdmin

from .models import Post, Review


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    Admin Class for the management of Service Posts

    """
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


class ReviewAdmin(admin.ModelAdmin):
    """
    Admin Class for the management of Review Posts

    """
    list_display = ('body', 'post', 'created_on', 'active', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'body')
    actions = ['approve_reviews']

    def approve_reviews(self, request, queryset):
        """Function for approval updates"""
        queryset.update(approved=True)


admin.site.register(Review, ReviewAdmin)


class UserUpdateForm(forms.ModelForm):
    """
    Form for profile name update
    """
    email = forms.EmailField()

    class Meta:
        """Fields available for update in user profile"""
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
