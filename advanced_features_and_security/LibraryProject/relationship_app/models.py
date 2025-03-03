from django.db import models
from django.contrib.auth.models import User
<<<<<<< HEAD
from django.conf import settings


=======

# Create your models here.
>>>>>>> 100fafa8c433f18a4f4d04a8da6a7d3056d4d76d
class Author(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Book(models.Model):
    title = (models.Model)
    author = models.ForeignKey(Author, on_delete= models.CASCADE)
    def __str__(self):
        return self.title + self.author.name
        

class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book, related_name= "library")

    def __str__(self):
        return self.name 


class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete= models.CASCADE)
    def __str__(self):
        return self.name

class UserProfile(models.Model):
<<<<<<< HEAD
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
=======
    user = models.OneToOneField(User, on_delete=models.CASCADE)
>>>>>>> 100fafa8c433f18a4f4d04a8da6a7d3056d4d76d
    role_choices = [
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    ]
    role = models.CharField(max_length=20, choices=role_choices)

class Meta:
        permissions = [
            ("can_add_book", "Can add book"),
            ("can_change_book", "Can change book"),
            ("can_delete_book", "Can delete book"),
        ]








