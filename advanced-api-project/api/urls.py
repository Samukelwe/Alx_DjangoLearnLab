
from django.urls import path
from .views import (
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView,
)

urlpatterns = [
    path("books/", BookListView.as_view(), name="books-list"),
    path("book/<int:pk>/", BookDetailView.as_view(), name="book-list"),
    path("book/", BookCreateView.as_view(), name="create-book"),
    path("book-update/<int:pk>/", BookUpdateView.as_view(), name="book-update"),
    path("delete/<int:pk>/", BookDeleteView.as_view(), name="book-delete"),
]


