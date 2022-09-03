from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
class Customer(models.Model):
   username=models.CharField(max_length=200,null=True,blank=True)
   first_name=models.CharField(max_length=200,null=True,blank=True)
   last_name=models.CharField(max_length=200,null=True,blank=True)
   email=models.CharField(max_length=200,null=True,blank=True)
   password=models.CharField(max_length=200,null=True)
   def register(self):
       self.save()
   def isExists(self):
        if Customer.objects.filter(email=self.email):
           return True
        else:
           return False
   def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False
        
class Item(models.Model):
    name = models.CharField(max_length=200,null=True)
    img  = models.ImageField(upload_to='pictures')
    description = models.TextField()
    slug=models.SlugField(unique=True)
    price = models.FloatField()
    quantity = models.IntegerField()
    timestamp=models.DateTimeField()
    def __str__(self):
        return self.name
    class Meta:
        unique_together=('name','slug')
    
    @staticmethod
    def get_all_items():
        return Item.objects.all()
    def get_all_items_ById(ids):
        try:
            return Item.objects.filter(id__in=ids)
        except:
            return False

   
    

    