from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import render
from book.models import Book, Author
from .serializers import AuthorSerializer, BookSerializer


# Create your views here.

@api_view(['GET', 'POST'])
def list_authors(request):
    if request.method == 'GET':
        authors = Author.objects.all()
        serializers = AuthorSerializer(authors, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        deserialize = AuthorSerializer(data=request.data)  # this is still serialized under thr hood.
        deserialize.is_valid(raise_exception=True)
        deserialize.validated_data()
        deserialize.save()
        return Response("Successful", status=status.HTTP_201_CREATED)


@api_view()
def list_books(request):
    books = Book.objects.all()
    serializers = BookSerializer(books, many=True, context={'request': request})
    return Response(serializers.data, status=status.HTTP_200_OK)


@api_view()
def welcome(request):
    return Response("ok")


@api_view()
def author_detail(request, pk):
    author = Author.objects.get(pk=pk)
    serializer = AuthorSerializer(author)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view()
def book_detail(request, pk):
    book = Book.objects.get(pk=pk)
    serializer = BookSerializer(book)
    return Response(serializer.data, status=status.HTTP_200_OK)
