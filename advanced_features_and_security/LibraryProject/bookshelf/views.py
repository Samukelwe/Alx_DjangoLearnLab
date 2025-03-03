from django.shortcuts import render
from django.http import HttpResponse

<<<<<<< HEAD
from django.contrib.auth.decorators import permission_required

@permission_required('app_name.can_edit', raise_exception=True)
def edit_view(request):
    
=======


>>>>>>> 100fafa8c433f18a4f4d04a8da6a7d3056d4d76d


def book_list(request):
    
    return HttpResponse("This is the book list view")

def books(request):
    
    return HttpResponse("This is the books view")


from django.contrib.auth.decorators import permission_required

@permission_required('app_name.can_view_books')
def book_list(request):
    # View logic

@permission_required('app_name.can_edit_books')
def books(request):
    # View logic