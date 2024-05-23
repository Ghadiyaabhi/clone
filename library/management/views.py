from django.shortcuts import render
from .models import Book,Borrower,ReturningBook,Reservation,BookRequest,author
from .serializer import Bookserializer,Borrowerserializer,ReturningBookSerializer,ReservationSerializer,BookRequestSerializer,AuthorSerializer            
from rest_framework.response import Response
from rest_framework.views  import APIView
from datetime import datetime
from rest_framework import status

class libraryBookView(APIView):
    def get(self,request):
        books = Book.objects.all()
        serializer=Bookserializer(books,many=True)
        return Response(serializer.data)
    
    def  post(self,request):
        serializer=Bookserializer(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response("Saved to database",status=201)
        else:
            return Response(serializer.errors,status=400)


        


class libraryBorrowerView(APIView):
    def get(self,bookid):
        try:
            book=Book.objects.get(pk=bookid)
            borrowers=Borrower.objects.filter(book=book)
            serializer=Borrowerserializer(borrowers, many=True)
            return Response(serializer.data)
        except Book.DoesNotExist:
            return Response({"error":"Invalid Book Id"}, status=404)  
        

     
    def post(self,request):
        if  not Borrower.objects.filter(pk=request.data['bookid']).exists():
            return Response({'message':'The borrower doesnot exist'},status=400)
         




class returningBookView(APIView):
    def post(self, request):
        try:
            borrower_id = int(request.data.get('borrowerid'))
            book_id = int(request.data.get('bookid'))
            borrower = Borrower.objects.get(pk=borrower_id)
            book = Book.objects.get(pk=book_id)
            return_date = datetime.now()
           
            return Response('Book returned successfully', status=200)
        except Exception as e:
            return Response('Entered data is incorrect or an error occurred', status=400)
    




class ReservationView(APIView):
    def post(self, request):
        reservations = Reservation.objects.all()
        serialized_reservations = ReservationSerializer(reservations, many=True)
        return Response(serialized_reservations.data)


class BookRequestView(APIView):
    def post(self, request):
        
        serializer = BookRequestSerializer(data=request.data)
        if serializer.is_valid():
            
            user = request.user
            
            book_name = serializer.data.get('book')
            
            try:
                
                book = Book.objects.get(title=book_name)
            except Book.DoesNotExist:
                return Response({'message': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)
          
            book_request = BookRequest(user=user, book=book)
            book_request.save()
            
            return Response({'message': 'Book request created'}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      
        

class AuthorView(APIView):
    def get(self, request, author_id):
        try:
            author_instance = author.objects.get(pk=author_id)
            serializer = AuthorSerializer(author_instance)
            return Response(serializer.data)
        except author.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        

class SearchBookView(APIView):
    def searchBooksByAuthor(request, author):
        books = Book.objects.filter(author__contains=author)
        serializer = Bookserializer(books, many=True)
        return Response(serializer.data)