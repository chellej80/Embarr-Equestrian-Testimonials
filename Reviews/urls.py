from . import views
from django.urls import path, include
#from .views import CommentDeleteView


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('delete_comment/<int:comment_id>', views.delete_comment,
         name='delete_comment'),
    path('edit_comment/<int:pk>', views.EditComment.as_view(),
         name='edit_comment'),
    path('search/',views.search, name='search'),
    path('accounts/', include('allauth.urls')),
    #path('user/', views.profile, name= 'user_profile'),
    path('profile', views.profile_view, name='profile'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    #path('<slug:slug>/', views.post_detail, name='post_detail'),
    
    #path('post/edit/<int:pk>/', views.PostEditView.as_view(), name='post_edit'),
    #path('post/delete/<int:pk>/', views.PostDeleteView.as_view(), name='post_delete'),
    #path('post/<int:post_pk>/comment/delete/<int:pk>/', views.commentDeleteView.as_view(), name='post_delete'),
    #path('blog/<slug:slug>/delete_comment/',views.PostCommentDeleteView.as_view(), name='post_delete'),
    
]