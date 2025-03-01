from django.contrib import admin
from .models import Book
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ['title','author','publication_year']
    search_fields = ['title','author']
    list_filter=['publication_year']
    list_filter = ['publication_year']

admin.site.register(Book, BookAdmin)


class CustomUserAdmin(UserAdmin):
    # Custom admin configurations for the custom user model

 admin.site.register(CustomUser, CustomUserAdmin)
