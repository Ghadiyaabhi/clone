from django.contrib import admin
from management.models import Book,Borrower,ReturningBook,Reservation,BookRequest,author

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    model = Book
    list_display = ['title', 'author', 'available','id']

@admin.register(Borrower)
class BorrowerAdmin(admin.ModelAdmin):
    model = Borrower
    list_display = ['name','id']

@admin.register(ReturningBook)
class ReturningBookAdmin(admin.ModelAdmin):
    model = ReturningBook
    list_display = ['returned_book','returning_date','borrower']

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    model = Reservation
    list_display = ['user','reservation_date','is_active']

@admin.register(BookRequest)
class BookRequestAdmin(admin.ModelAdmin):
    model = BookRequest
    list_display = ['requester','requested_book','request_date']


@admin.register(author)
class authorAdmin(admin.ModelAdmin):
    model = author
    list_display = ['user','id']
