from typing import Any
from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    email = models.EmailField(max_length=30)


    def __init__(self):
        return self.name