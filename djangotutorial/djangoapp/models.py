from django.db import models
from django.utils import timezone

# Create your models here.
class AppVarity(models.Model):
    APP_TYPE_CHOICE = [
        ('SM', 'Social Media'),
        ('EC','E-commerce'),
        ('FH','Fitness and Health'),
        ('BK','Banking'),
    ]
    name= models.CharField(max_length=100)
    image = models.ImageField(upload_to='apps/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=APP_TYPE_CHOICE)
    descriptions = models.TextField(default='')

    def __str__(self):
          return f"{self.name}"