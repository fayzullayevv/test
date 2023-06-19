from django.db import models

# Create your models here.

class RegisterModell(models.Model):
  name = models.CharField(max_length=100)
  surname = models.CharField(max_length=100)
  school = models.PositiveBigIntegerField()
  clas = models.PositiveBigIntegerField()
  age = models.PositiveBigIntegerField()
  course = models.CharField(max_length=100)

  def __str__(self):
    return self.name
  

