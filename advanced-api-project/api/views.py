

from rest_framework import filters
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListAPIView):
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fileds = ["title", "author", "publication_year"]
    filter_backends = [filters.SearchFilter]
    search_fields = ["title", "author"]
    filter_backends = [rest_framework.filters.OrderingFilter]
    ordering_fields = ["title", "publication_year"]

