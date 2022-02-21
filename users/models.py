from django.db import models

# Create your models here.

class UserDeatils(models.Model):
    name = models.CharField(max_length=500)
    phone_number = models.CharField(max_length=50)
    age = models.CharField(max_length=500)
    email = models.EmailField()
    password = models.CharField(max_length=50000)

    def __str__(self):
        return self.name