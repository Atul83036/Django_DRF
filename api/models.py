from django.db import models
from django.contrib.auth.models import User

class Column(models.Model):
    title = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Card(models.Model):
    title = models.CharField(max_length=100)
    description=models.TextField()
    column = models.ForeignKey(Column, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
