from django.db import models
from brand.models import Brand
from django.contrib.auth.models import User

# Create your models here.

class Car(models.Model):
    carid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    quantity = models.IntegerField()
    description = models.TextField()
    
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'uploads', blank = True, null = True)

    def __str__(self):
        return self.name
    

class ProfileCar(models.Model):
    carid = models.IntegerField()
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    quantity = models.IntegerField()
    description = models.TextField()
    
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'uploads', blank = True, null = True)

    def __str__(self):
        return self.name
    

class Comment(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name= 'comments')
    name = models.CharField(max_length=30)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comments by {self.name}"

