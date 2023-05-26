from django_filters import FilterSet
from .models import Author, Book


class AuthorFilter(FilterSet):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name']


class BookFilter(FilterSet):
    class Meta:
        model = Book
        fields = ['title', 'author']
