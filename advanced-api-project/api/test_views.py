from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Book

class BookAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.book_data = {'title': 'Sample Book', 'author': 'John Doe', 'publication_year': 2022}
        self.book = Book.objects.create(title='Test Book', author='Jane Smith', publication_year=2020)

    def test_create_book(self):
        response = self.client.post(reverse('book-list'), self.book_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_book(self):
        response = self.client.put(reverse('book-detail', kwargs={'pk': self.book.id}), {'title': 'Updated Book'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_book(self):
        response = self.client.delete(reverse('book-detail', kwargs={'pk': self.book.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_filter_books(self):
        response = self.client.get(reverse('book-list') + '?author=John Doe')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_search_books(self):
        response = self.client.get(reverse('book-list') + '?search=Sample Book')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_order_books(self):
        response = self.client.get(reverse('book-list') + '?ordering=-publication_year')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    