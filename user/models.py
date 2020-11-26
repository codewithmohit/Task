from django.db import models

# Create your models here.
class Student(models.Model):

    objects = None
    f_name= models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    email=models.CharField(max_length=50,default="",primary_key=True)
    password=models.CharField(max_length=50,default="")
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=50)
    phone = models.CharField(max_length=50,default="",unique=True)
    groups = models.ManyToManyField('auth.Group', blank=True, verbose_name=('Groups'))

    def __str__(self):
        return self.f_name