from django.db import models

from oneauthor.models import Author

class Book(models.Model):
    title = models.CharField(max_length=255, unique=False)
    text = models.TextField()
    publication_date = models.DateTimeField('Book publication datetime', null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
