from django.urls import path

from book import views

urlpatterns = [
    path("authors/", views.list_authors, name='home'),
    path("welcome/", views.welcome)
]