from django.db import models

# Create your models here.
class Idea(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    