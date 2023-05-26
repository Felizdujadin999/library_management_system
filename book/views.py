from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from book.models import Book, Author
from .serializers import AuthorSerializer, BookSerializer
from .pagination import DefaultPagination
from .filters import AuthorFilter, BookFilter


# Create your views here.

class AuthorListViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    pagination_class = DefaultPagination
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = AuthorFilter
    search_fields = ['first_name', 'last_name']


class BookListViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = DefaultPagination
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = BookFilter
    search_fields = ['title']


# class AuthorList(ListCreateAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer


# class BookList(ListCreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#
#     def get_serializer_context(self):
#         return {'request': self.request}

# def get_queryset(self):
#     return Author.objects.all()
#
# def get_serializer_class(self):
#     return AuthorSerializer


# class AuthorView(APIView):
#     def get(self, request):
#         authors = Author.objects.all()
#         serializers = AuthorSerializer(authors, many=True)
#         return Response(serializers.data, status=status.HTTP_200_OK)
#
#     def post(self, request):
#         deserialize = BookSerializer(data=request.data)
#         deserialize.is_valid(raise_exception=True)
#         deserialize.save()
#         return Response("Successful", status=status.HTTP_201_CREATED)


# class AuthorDetail(RetrieveUpdateDestroyAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer


# class BookDetail(RetrieveUpdateDestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


# class AuthorDetailView(APIView):
#     def get(self, request, pk):
#         author = get_object_or_404(Author, pk=pk)
#         serializer = AuthorSerializer(author)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def put(self, request, pk):
#         author = get_object_or_404(Author, pk=pk)
#         serializer = AuthorSerializer(author, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#     def delete(self, request, pk):
#         author = get_object_or_404(Author, pk=pk)
#         if author.book_author.count() > 0:
#             return Response({"error": "Author is associated with a book and cannot be deleted"},
#                             status=status.HTTP_405_METHOD_NOT_ALLOWED)
#         author.delete()
#         return Response("deleted successfully", status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET', 'POST'])
# def list_authors(request):
#     if request.method == 'GET':
#         authors = Author.objects.all()
#         serializers = AuthorSerializer(authors, many=True)
#         return Response(serializers.data, status=status.HTTP_200_OK)
#     elif request.method == 'POST':
#         deserialize = AuthorSerializer(data=request.data)  # this is still serialized under thr hood.
#         deserialize.is_valid(raise_exception=True)
#         deserialize.save()
#         return Response("Successful", status=status.HTTP_201_CREATED)


# @api_view(['GET', 'POST'])
# def list_books(request):
#     if request.method == 'GET':
#         books = Book.objects.all()
#         serializers = BookSerializer(books, many=True, context={'request': request})
#         return Response(serializers.data, status=status.HTTP_200_OK)
#     elif request.method == 'POST':
#         deserialize = BookSerializer(data=request.data)  # this is still serialized under thr hood.
#         deserialize.is_valid(raise_exception=True)
#         deserialize.save()
#         return Response("Successful", status=status.HTTP_201_CREATED)


@api_view()
def welcome(request):
    return Response("ok")

# @api_view(['GET', 'DELETE', 'PUT'])
# def author_detail(request, pk):
#     author = get_object_or_404(Author, pk=pk)
#     if request.method == 'GET':
#         serializer = AuthorSerializer(author)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'PUT':
#         serializer = AuthorSerializer(author, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response("detail updated", status=status.HTTP_200_OK)
#     elif request.method == 'DELETE':
#         if author.book_author.count() > 0:
#             return Response({"error": "Author is associated with a book and cannot be deleted"},
#                             status=status.HTTP_405_METHOD_NOT_ALLOWED)
#         author.delete()
#         return Response("deleted successfully", status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET', 'DELETE', 'PUT'])
# def book_detail(request, pk):
#     book = get_object_or_404(Book, pk=pk)
#     if request.method == 'GET':
#         serializer = BookSerializer(book)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'PUT':
#         serializer = BookSerializer(book, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response("detail updated", status=status.HTTP_200_OK)
#     elif request.method == 'DELETE':
#         book.delete()
#         return Response("deleted successfully", status=status.HTTP_204_NO_CONTENT)
