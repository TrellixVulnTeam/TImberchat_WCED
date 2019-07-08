from django.db import models

class Chat(models.Model):
    name = models.CharField(max_length=255, null= True)
    code = models.BigIntegerField(default="0")
    user_id = models.BigIntegerField(default=0)
    text = models.TextField(null=True, blank=True)
    time = models.DateTimeField(auto_now=True)

