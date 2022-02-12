from django.db import models

# Create your models here.
# Create your models here.

class Crud(models.Model):

        name = models.CharField(max_length=50)

        description = models.CharField(max_length=250,blank=True)

        price = models.FloatField()

        created = models.DateTimeField(auto_now_add=True)

        modified = models.DateTimeField(auto_now=True)