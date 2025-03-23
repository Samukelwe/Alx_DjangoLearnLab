from django.urls import path
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
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

    
]

