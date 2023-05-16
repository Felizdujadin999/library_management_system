from uuid import uuid4
from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True)


class Book(models.Model):
    LANGUAGE_CHOICES = [
        ('Y', "YORUBA"),
        ('H', "HAUSA"),
        ('I', "IGBO"),
        ('E', "ENGLISH")
    ]

    GENRE_CHOICES = [
        ('FIC', "FICTION"),
        ('POL', "POLITICS"),
        ('FIN', "FINANCE"),
        ('ROM', "ROMANCE")
    ]
    title = models.CharField(max_length=225, blank=False, null=False)
    isbn = models.CharField(max_length=15, blank=False, null=False)
    description = models.CharField(max_length=300, blank=False, null=False)
    date_added = models.DateTimeField(blank=True, null=False)
    genre = models.CharField(max_length=15, choices=GENRE_CHOICES)
    language = models.CharField(max_length=15, choices=LANGUAGE_CHOICES)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    author = models.ForeignKey('Author', on_delete=models.PROTECT, blank=False, null=False)

    def __str__(self):
        return f"""
        title: {self.title}, author: {self.author}"""


class Author(models.Model):
    first_name = models.CharField(max_length=225, blank=False, null=False)
    last_name = models.CharField(max_length=225, blank=False, null=False)
    email = models.EmailField(blank=True, default="")
    date_of_birth = models.DateField(blank=True, null=True)
    date_of_death = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"""
        first_name: {self.first_name}
        last_name: {self.last_name}
        email: {self.email}
        date_of_birth: {self.date_of_birth}
        """


class BookInstance(models.Model):
    STATUS_CHOICES = [
        ('AVAILABLE', 'A'),
        ('BORROWED', 'B')
    ]
    due_back = models.DateField()
    unique_id = models.UUIDField(primary_key=True, default=uuid4)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='A')
    book = models.ForeignKey(Book, on_delete=models.PROTECT)
    user = models.OneToOneField(User, on_delete=models.PROTECT)

    def __str__(self):
        return f"""
        due_back: {self.due_back}
        status: {self.status}
        book: {self.book}
        """
