from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Pizza(models.Model):
    pizza_name = models.CharField(max_length = 200)
    date_added = models.DateTimeField(auto_now_add=True)
    #owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.pizza_name

class Topping(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    topping_name = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.topping_name[:50]}"

class Profile(models.Model):
    first_name = models.CharField(max_length=200,blank=True)
    last_name = models.CharField(max_length=200,blank=True)
    email = models.EmailField(max_length=300,blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.user.username}"

STATUS_CHOICES = (
    ('sent','sent'),
    ('accepted','accepted')
)

class Comment(models.Model):
    post = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    username = models.ForeignKey(User, related_name='details', on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self):
        return self.text

class MyImages(models.Model):
    upload = models.ImageField(upload_to = 'uploads/')
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)



