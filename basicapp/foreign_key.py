from django.db import models
import uuid


class TestForeignkey(models.Model):
    objects = None
    id = models.UUIDField(default=uuid.uuid4(), max_length=125, primary_key=True, null=False)
    signup = models.ForeignKey("SignUp", on_delete=models.CASCADE)
