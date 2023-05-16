from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from book.models import Book, Author


def list_authors(request):
    authors = Author.objects.all()
    return render(request, 'book/book.html', {"authors": authors})


def welcome(request):
    return HttpResponse("ok")
