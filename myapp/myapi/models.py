from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=15)
    image = models.ImageField(upload_to='images', default='images/default.png')

    def __str__(self):
        return self.title


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Item, related_name='cart_items')

    def __str__(self):
        return self.user.username
