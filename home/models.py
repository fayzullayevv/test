from django.db import models

# Create your models here.

class HomeModel(models.Model):
  name = models.CharField(max_length=100)
  surname = models.CharField(max_length=100)
  email = models.EmailField(max_length=100)

  def __str__(self):
    return self.name