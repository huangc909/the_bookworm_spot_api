from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user, authenticate, login, logout
from django.middleware.csrf import get_token

from ..models.book import Book
from ..serializers import BookSerializer, UserSerializer

class Books(generics.ListCreateAPIView):
    permission_classes=(isAuthenticated,)
    def get(self, request):
        """Index request"""
        # books = Book.objects.all()
        books = Book.objects.filter(owner=request.user.id)
        data = BookSerializer(books, many=True).data
        return Response(data)

    serializer_class = BookSerializer
    def post(self, request):
        """Create request"""
        # Add user to request object
        request.data['book']['owner'] = request.user.id
        # Serialize/create book
        book = BookSerializer(data=request.data['book'])
        if book.is_valid():
            b = book.save()
            return Response(book.data, status=status.HTTP_201_CREATED)
        else:
            return Response(book.errors, status=status.HTTP_400_BAD_REQUEST)

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    def get(self, request, pk):
        """Show request"""
        book = get_object_or_404(Book, pk=pk)
        data = BookSerializer(book).data
        if not request.user.id == data['owner']:
            raise PermissionDenied('Unauthorized, you do not own this book.')
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
