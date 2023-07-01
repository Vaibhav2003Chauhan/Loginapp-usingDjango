from django.db import models

# Create your models here.
class User(models.Model):
    username=models.CharField(max_length=90)
    email=models.CharField(max_length=200,unique=True)
    password=models.CharField(max_length=10)
    cpassword=models.CharField(max_length=10)

    def __str__(self):
        return self.username
    

