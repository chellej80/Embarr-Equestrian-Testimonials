from .models import *
from .forms import CommentForm, searchForm, UserUpdateForm
from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import(render, get_object_or_404, reverse, redirect, resolve_url)
from django.http import HttpResponseRedirect



class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 2


def post_detail(request, slug):
    template_name = 'post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            new_comment.author = request.user
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(
        request,
        'post_detail.html',
        {
            'post': post,
            'comments': comments,
            'new_comment': new_comment,
            'comment_form': comment_form
        },
    )


def search_post(request):
    form = searchForm()
    q = ''
    results =[]

    if 'q' in request.GET:
        form = searchForm(request.GET)
        if form.is_valid():
            q = form.cleaned_data['q']
            results = Post.objects.filter(title=q)
    
    return render(request, 'search.html',
                    {'form':form,
                     'q':q, 
                     'results': results})

@login_required
def profile_view(request):
    """
    Renders the profile page
    """
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        #profile_form = ProfileUpdateForm(
            #request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid():
            user_form.save()
            #profile_form.save()
            messages.success(request, 'Your account has been updated!')
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        #profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        #'profile_form': profile_form,
    }
    return render(request, 'profile.html', context)
    
