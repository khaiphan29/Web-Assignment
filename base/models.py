from distutils.command.upload import upload
from random import choices
from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length= 200, default='Updating...')
    path = models.SlugField(default= '')
    brand = models.CharField(
        max_length= 20, 
        choices = [('AP', 'Apple'), ('SS', 'Samsung')],
        default='AP')
    image = models.ImageField(upload_to = 'img/product_img', null = True, blank = True)
    created = models.DateTimeField(auto_now_add=True)
    capacity = models.CharField(max_length= 200, default='Updating...')
    minprice = models.PositiveIntegerField(default= 0)
    screensize = models.CharField(max_length= 200, default='Updating...')
    screenres = models.CharField(max_length= 200, default='Updating...')
    os = models.CharField(max_length= 200, default='Updating...')
    chip = models.CharField(max_length= 200, default='Updating...')
    camera = models.CharField(max_length= 200, default='Updating...')
    videorecording = models.TextField(null=True, blank=True)
    power = models.TextField(null=True, blank=True)
    box = models.CharField(max_length= 200, default='Updating...')

    def __str__(self):
        return self.name
