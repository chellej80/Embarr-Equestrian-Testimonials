from .models import *
from .forms import CommentForm, UserUpdateForm
from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.views.generic import UpdateView
# from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import(render, get_object_or_404, reverse, redirect, resolve_url)
from django.http import HttpResponseRedirect
from django.db.models import Q




class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 2

class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
            
            },
        )
    
    def post(self, request, slug, *args, **kwargs):

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        comment_form = CommentForm(data=request.POST)
        new_comment = None
        # Comment posted
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
        else:
            comment_form = CommentForm()

        return render(request, 'post_detail.html', 
                        {'post': post,
                        'comments': comments,
                        'comment_form': comment_form,
                        'new_comment': new_comment})


def search(request):
    """
    search results
    """
    queryset = Post.objects.all()
    if request.method == "POST":
        searched = request.POST["searched"]
        results = Post.objects.filter(
                Q(title__contains=searched)  
            ).distinct()
        context = {
               'queryset': queryset
        }

        return render(request, 'search.html', {
            'results': results, 'searched': searched})
    else:

        return render(request, 'search.html', context)



@login_required
def profile_view(request):
    
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

@login_required
def delete_comment(request, comment_id):
    """
    Function to Delete comment
    """
    comment = get_object_or_404(Comment, id=comment_id)
    comment.delete()
    messages.success(request, 'Your comment was deleted successfully')
    return HttpResponseRedirect(reverse(
        'post_detail', args=[comment.post.slug]))


class EditComment(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """
    Edit comment
    """
    model = Comment
    template_name = 'edit_comment.html'
    form_class = CommentForm
    success_message = 'Your comment was updated'
    
