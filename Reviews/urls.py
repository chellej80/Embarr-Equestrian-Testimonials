from django.urls import path, include
from . import views


"""url paths for Reviews App"""


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('delete_review/<int:review_id>', views.delete_review,
         name='delete_review'),
    path('edit_review/<int:pk>', views.EditReview.as_view(),
         name='edit_review'),
    path('search/', views.search, name='search'),
    path('accounts/', include('allauth.urls')),

    path('profile', views.profile_view, name='profile'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),

]
