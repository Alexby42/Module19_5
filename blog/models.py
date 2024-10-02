from django.db import models
# Create your models here.

class Buyer(models.Model):
    objects = None
    name = models.CharField(max_length=100)
    balance = models.DecimalField(decimal_places=2, max_digits=6)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Game(models.Model):
    objects = None
    title = models.CharField(max_length=200)
    cost = models.DecimalField(decimal_places=2, max_digits=6)
    size = models.DecimalField(decimal_places=2, max_digits=10)
    description = models.TextField()
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer, related_name='title')

    def __str__(self):
        return self.title

class Posts(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(default='')
    date = models.DateTimeField(auto_now=False)

    def __str__(self):
        return self.title

class User(models.Model):
    username = models.CharField(max_length=10)
    age = models.IntegerField()

    def __str__(self):
        return self.username