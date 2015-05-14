from django.contrib.auth.models import User
from django.db import models


class Restaurant(models.Model):
    created_by = models.ForeignKey(User, related_name='restaurant_created_by')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_by = models.ForeignKey(User, related_name='restaurant_modified_by')
    modified_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=32, unique=True)
    phone_number = models.CharField(max_length=16)
    address = models.TextField()
    website = models.URLField()
    logo = models.URLField()

    class Meta:
        ordering = ['name']
