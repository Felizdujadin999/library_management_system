from decimal import Decimal

from rest_framework import serializers
from .models import Author, Book


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'date_of_birth']


class BookSerializer(serializers.ModelSerializer):
    # author = AuthorSerializer()
    class Meta:
        model = Book
        fields = ['title', 'description', 'genre', 'language', 'price', 'book_number', 'discount_price', 'author']

    author = serializers.HyperlinkedRelatedField(
        queryset= Author.objects.all(),
        view_name='author-detail'
    )
    book_number = serializers.CharField(max_length=10, source='isbn')
    discount_price = serializers.SerializerMethodField(method_name='calculating_discount')

    def calculating_discount(self, price: Book):
        return price.price * Decimal(0.1)

    # author = serializers.ForeignKey('Author', blank=False, null=False)
