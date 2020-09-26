from django.db import models


class Teacher(models.Model):
    name = models.CharField(max_length=30)
    subject_Name = models.CharField(max_length=40)
    qualification = models.CharField(max_length=100)

    def __str__(self):
        return self.name+" teaches "+self.subject_Name