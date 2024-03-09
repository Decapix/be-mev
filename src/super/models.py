from django.db import models
import uuid

# Create your models here.


class Profile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField(max_length=100)
    description = models.TextField(max_length=400)
    role = models.TextField(max_length=250)
    show = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.ask}"