from django.db import models


class Teacher(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    subject_Name = models.CharField(max_length=40)
    password = models.CharField(max_length=40,default='')
    qualification = models.CharField(max_length=100)
    image = models.ImageField(upload_to='teacher/images',blank=True, default='')

    def __str__(self):
        return self.name+" teaches "+self.subject_Name+" WITH ID"+str(self.id)