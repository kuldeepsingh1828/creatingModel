from django.db import models

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    book_Name = models.CharField(max_length=200)
    author_Name = models.CharField(max_length=100)
    descripton = models.CharField(max_length=400)
    price = models.CharField(max_length=10)

    def __str__(self):
        return self.book_Name+" by "+self.author_Name