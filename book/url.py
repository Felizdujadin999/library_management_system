from django.urls import path

from book import views

urlpatterns = [
    path("authors/", views.list_authors),
    path("books/", views.list_books),
    path("welcome/", views.welcome),
    path("authors/<int:pk>/", views.author_detail, name='author-detail'),
    path("books/<int:pk>/", views.book_detail)
]