from django.db import models

# Create your models here.

class Unhash(models.Model): 
    hashInput = models.CharField(max_length=200)
    hashType = models.CharField(max_length=200)

class hashcatmode(models.Model): 
    number = models.IntegerField()
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)

    def __str__(self): 
        return f"{self.name},{self.category}"