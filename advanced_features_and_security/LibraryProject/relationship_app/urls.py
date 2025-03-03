from django.urls import path
from .views import list_books, LibraryDetailView
from django.contrib.auth.views import LoginView, LogoutView 
<<<<<<< HEAD

=======
from .views import CustomLoginView, CustomLogoutView, CustomRegisterView
>>>>>>> 100fafa8c433f18a4f4d04a8da6a7d3056d4d76d

from .views import list_books
from .views import LibraryDetailView
from . import views


urlpatterns = [
    path("", list_books, name="list_books"),
    path("library/<pk>/", LibraryDetailView.as_view(), name="library_detail"),
    path(
        "relationship_app/login",
        LoginView.as_view(template_name="registration/login.html"),
        name="login",
    ),
    path(
        "relationship_app/logout/",
        LogoutView.as_view(template_name="registration/login.html"),
        name="logout",
    ),
    path("relationship_app/register/", views.register, name="register"),
<<<<<<< HEAD
   
    
=======
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', CustomRegisterView.as_view(), name='register'),
>>>>>>> 100fafa8c433f18a4f4d04a8da6a7d3056d4d76d
     path('admin/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),
     path('add_book/', views.add_book, name='add_book'),
    path('edit_book/<int:book_id>/', views.edit_book, name='edit_book'),
    path('delete_book/<int:book_id>/', views.delete_book, name='delete_book'),

]












