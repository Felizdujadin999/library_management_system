from django.urls import path, include
from rest_framework.routers import SimpleRouter

from book import views

router = SimpleRouter()
router.register('authors', views.AuthorListViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path("authors/", views.list_authors), # functional way of calling it
    # path("authors/", views.AuthorView.as_view()),
    path("authors/", views.AuthorList.as_view()),
    path("books/", views.BookList.as_view()),
    # path("books/", views.list_books),
    path("welcome/", views.welcome),
    # path("authors/<int:pk>/", views.author_detail, name='author-detail'), # functional way as well
    # path("authors/<int:pk>/", views.AuthorDetailView.as_view(), name='author-detail'),
    path("authors/<int:pk>/", views.AuthorDetail.as_view(), name='author-detail'),
    path("books/<int:pk>/", views.BookDetail.as_view()),
    # path("books/<int:pk>/", views.book_detail)
]
