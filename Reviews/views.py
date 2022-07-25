from .models import Post, Review
# from django.contrib.auth.models import User
from .forms import ReviewForm, UserUpdateForm
from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.views.generic import UpdateView
# from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import(render, get_object_or_404,  
                             reverse, redirect, resolve_url)
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
        reviews = post.reviews.filter(approved=True).order_by("-created_on")

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "reviews": reviews,
            
            },
        )
    
    def post(self, request, slug, *args, **kwargs):

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        reviews = post.reviews.filter(approved=True).order_by("-created_on")
        review_form = ReviewForm(data=request.POST)
       
        new_review = None

        # Review posted
        if review_form.is_valid():

            review_form.instance.name = request.user.username
            # Create Comment object but don't save to database yet
            new_review = review_form.save(commit=False)
            # Assign the current post to the comment
            new_review.post = post
            # Save the comment to the database
            new_review.save()
           
        else:
            review_form = ReviewForm()

        return render(request, 'post_detail.html', 
                      {'post': post,
                       'reviews': reviews,
                       'review_form': review_form,
                       'new_review': new_review})


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
        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Your account has been updated!')
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        
    context = {
        'user_form': user_form,
        
    }
    return render(request, 'profile.html', context)


@login_required
def delete_review(request, review_id):
    """
    Function to Delete comment
    """
    review = get_object_or_404(Review, id=review_id)
    review.delete()
    messages.success(request, 'Your Review was deleted successfully')
    return HttpResponseRedirect(reverse(
        'post_detail', args=[review.post.slug]))


class EditReview(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """
    Edit Review
    """
    model = Review
    template_name = 'edit_review.html'
    form_class = ReviewForm
    success_message = 'Your Review was updated'
