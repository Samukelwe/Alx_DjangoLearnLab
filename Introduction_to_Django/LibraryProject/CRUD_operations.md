from bookshelf.models import Book
book = Book.objects.create(title = '1984',author = 'George Orwell', publication_year = 1949)
book.save()
<!-- Book:1984 -->

retrive_book = Book.objects.get(title = "1984")

retrive_book.__dict__
 
<!-- {'id': 1,
 'title': '1984',
 'author': 'George Orwell',
 'publication_year': 1949} -->

 retrive_book = Book.objects.get(title = "1984")

retrive_book.__dict__
 
<!-- {'id': 1,
 'title': '1984',
 'author': 'George Orwell',
 'publication_year': 1949} -->

 from bookshelf.models import Book
retrive_book.delete()
(1, {'bookshelf.Book': 1})
Book.objects.all()
<!-- <QuerySet []> -->