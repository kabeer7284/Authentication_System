from django.db import models
from django.db.models import CharField


# Create your models here.
class Student(models.Model):
    #id = models.AutoField()
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.TextField()
    #image = models.ImageField(default=None)
    #file = models.FileField(default=None)

class Car(models.Model):
    car_name = models.CharField(max_length=500)
    speed = models.IntegerField(default=50)

    def __str__(self) -> str:
        return self.car_name

