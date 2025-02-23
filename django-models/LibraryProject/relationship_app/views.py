from django.shortcuts import render
from .models import Book
from django.views.generic.detail import DetailView

# Create your views here.
def list_books(request):
    book = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"book": book})

class LibraryDetailView(DetailView):
    model = Library
    template_name = library_detail.html
    context_object_name = "library"


