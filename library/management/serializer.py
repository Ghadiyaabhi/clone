from rest_framework import serializers
from .models import Book,Borrower,ReturningBook,Reservation,BookRequest,author



class Bookserializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"

class Borrowerserializer(serializers.ModelSerializer):
    class Meta:
        model = Borrower
        fields = "__all__"        


class ReturningBookSerializer(serializers.ModelSerializer):
    class Meta:
        model=ReturningBook
        fields="__all__"  

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = author
        fields = "__all__"


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = "__all__"  


class BookRequestSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = BookRequest
        fields = "__all__"              