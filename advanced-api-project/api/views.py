from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser  
from rest_framework.authentication import TokenAuthentication
from .models import Book
from .serializers import BookSerializer

# Create your views here.

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

 

class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows books to be viewed or edited.
    Only authenticated users can access this endpoint.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]  # Ensure only authenticated users can access this endpoint



