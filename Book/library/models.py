from django.db import models

class Book(models.Model):

    imageId = models.FileField(blank=True)
    isbn = models.CharField(max_length=200)
    bookName = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    page = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200)
    rating = models.FloatField(null=True)
    num_rating = models.IntegerField()
    isRated = models.BooleanField(default=False)
    numberOfCopys = models.IntegerField()
    MAX_COPYS = models.IntegerField()

    def __str__(self):
        return self.bookName




