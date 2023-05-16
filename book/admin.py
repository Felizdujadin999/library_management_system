from django.contrib import admin
from .models import Author, Book, User


# Register your models here.
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']
    list_filter = ['email', 'last_name']
    list_per_page = 20


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['isbn', 'author', 'title', 'language']
    list_filter = ['genre']
    list_per_page = 20


admin.site.register(User)
