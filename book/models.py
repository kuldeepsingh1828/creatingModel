from django.db import models


class Book2(models.Model):
    id = models.AutoField(primary_key=True)
    book_Name = models.CharField(max_length=200)
    author_Name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    pub_date = models.DateField()
    image = models.ImageField(upload_to='book/images', default='')

    def __str__(self):
        return self.book_Name+" by "+self.author_Name