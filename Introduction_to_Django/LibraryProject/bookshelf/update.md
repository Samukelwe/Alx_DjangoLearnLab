retrive_book.title =  "Nineteen Eighty-Four"
retrive_book.save()
book = Book.objects.get(id = retrive_book.id)
book.title
<!-- 'Nineteen Eighty-Four' -->

 