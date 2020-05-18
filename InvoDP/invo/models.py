from django.db import models

# Create your models here.
class Request(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.IntegerField()
    address = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    request_type = models.IntegerField()
    comment = models.CharField(max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
