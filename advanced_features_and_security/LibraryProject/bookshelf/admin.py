from django.contrib import admin
from .models import Book
<<<<<<< HEAD
=======
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
>>>>>>> 100fafa8c433f18a4f4d04a8da6a7d3056d4d76d


# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ['title','author','publication_year']
    search_fields = ['title','author']
    list_filter=['publication_year']
    list_filter = ['publication_year']

admin.site.register(Book, BookAdmin)
<<<<<<< HEAD
=======


class CustomUserAdmin(UserAdmin):
    # Custom admin configurations for the custom user model

 admin.site.register(CustomUser, CustomUserAdmin)
>>>>>>> 100fafa8c433f18a4f4d04a8da6a7d3056d4d76d
