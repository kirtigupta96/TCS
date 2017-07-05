from django.db import models
from django.utils import timezone

# Create your models here.
class Company(models.Model):
    name= models.CharField(max_length=100);
    about = models.CharField(max_length=1000);
    website = models.URLField();
