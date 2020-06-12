from django.db import models
import uuid


# Create your models here.

class SignUp(models.Model):
    objects = None
    id = models.UUIDField(default=uuid.uuid4(), max_length=125, primary_key=True, null=False)
    name = models.CharField(max_length=125, null=True)
    mobile_number = models.CharField(max_length=20, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
