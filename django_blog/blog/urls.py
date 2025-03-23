from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, register, profile_view, index

urlpatterns = [
    
    path('',index, name='home'),    
    path('login/', LoginView.as_view(template_name="registration/login.html"), name= 'login'),
    path('logout/',LogoutView.as_view(template_name="blog/logout.html"),name='logout'),
    path('register/',register,name='register'),
    path('profile/', profile_view, name='profile'),
    path('posts/', PostListView.as_view(), name='posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/comments/new/', views.CommentCreateView.as_view(), name='comment_create'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('comment/<int:pk>/update/', views.CommentUpdateView.as_view(), name='comment_update'),
    path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment_delete'),
    path('search/', views.search_view, name='search'),
    path('tags/<str:tag_name>/', views.tag_filter_view, name='tag_posts'),
    path('posts/<int:post_id>/comments/new/', views.add_comment_view, name='add_comment'),
    path('comments/<int:comment_id>/edit/', views.edit_comment_view, name='edit_comment'),
    path('comments/<int:comment_id>/delete/', views.delete_comment_view, name='delete_comment'),

    
    

    
]

