from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255, null=True)
    decription = models.TextField(null=True)
    images = models.CharField(max_length=255, null=True)
    created_by = models.BigIntegerField(default=0)
    updated_by = models.BigIntegerField(default=0)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(null=True)
    location = models.CharField(max_length=255, null=True)


