from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render
from book.models import Book, Author
from .serializers import AuthorSerializer

# Create your views here.


def list_authors(request):
    authors = Author.objects.all()
    return render(request, 'book/book.html', {"authors": authors})


@api_view()
def welcome(request):
    return Response("ok")


@api_view()
def author_detail(request, pk):
    author = Author.objects.get(pk=pk)
    serializer = AuthorSerializer(author)
    return Response(pk)
