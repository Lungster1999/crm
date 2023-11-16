from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

# Create your models here.
class Lead(models.Model):
    """
    Model definition for Lead.
    
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField(default=0)
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Agent(models.Model):
    """
    Model definition for Agent.
    
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
