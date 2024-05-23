from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=100)
    bookid = models.IntegerField
    author = models.CharField(max_length=100)
    available = models.BooleanField(default=True)

    def __str__(self) -> str:
        return str(self.author) + " | " + str(self.title)

class Borrower(models.Model):
    name = models.CharField(max_length=50)
    borrow_book = models.ManyToManyField(Book,related_name='borrowers')
    id = models.IntegerField
    
    def  __str__(self) -> str:
        return self.name
    
class author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    books = models.ManyToManyField(Book, related_name="authors")
    id = models.IntegerField


class ReturningBook(models.Model):
    returned_book = models.ForeignKey(Book,on_delete=models.CASCADE)
    returning_date = models.DateField
    borrower = models.ForeignKey(Borrower,on_delete=models.CASCADE)
            
class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    reservation_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

class BookRequest(models.Model):
    requester = models.ForeignKey(User, on_delete=models.CASCADE)
    requested_book = models.ForeignKey(Book, on_delete=models.CASCADE)
    request_date = models.DateTimeField(auto_now_add=True)
  
    def __str__(self)-> str:
        return str(self.requester) + " | " + str(self.requested_book)
        



