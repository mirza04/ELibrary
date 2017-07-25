from django.db import models

class Book(models.Model):

    imageId = models.FileField()
    isbn = models.CharField(max_length=200)
    bookName = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    page = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200)


    def __str__(self):
        return self.Book