from django.db import models
from django.urls import reverse

# Create your models here.
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__ (self):
        return str(self.name)
    def get_absolute_url(self):
        return reverse('Post')
    
class Post(models.Model):
    title = models.CharField(max_length=150)
    author= models.ForeignKey(User, on_delete=models.CASCADE)
    date_post = models.DateField(auto_now_add=True)
    offer = models.BooleanField(default=False)
    category = models.CharField(max_length=100,default='')
    body = models.TextField(default='')
    price = models.IntegerField()


    def __str__ (self):
        return self.title + " | " + str(self.author)
    
    
    def get_absolute_url(self):
        return reverse("Post")