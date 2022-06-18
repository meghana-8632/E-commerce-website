from django.db import models
from django.contrib.auth.models import User


class Items(models.Model):
    name = models.CharField(max_length=100)
    img  = models.ImageField(upload_to='pictures')
    description = models.TextField()
    price = models.IntegerField()
    quantity = models.IntegerField()
    
    def __str__(self):
        return self.name

    