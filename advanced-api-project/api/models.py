from django.db import models


class Author(models.Model):
    """"
    Model represents an author
    """
    name = models.CharField(max_length=100)

class Book(models.Model):
    """
    Model represents a book.
    """
    title = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

