from django.urls import path
from .views import BookList
from rest_framework.routers import DefaultRouter
from .views import BookViewSet
from api.views import BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path, include

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
     path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/create/', BookCreateView.as_view(), name='book-create'),
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),
    path('', include(router.urls)),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  
]




