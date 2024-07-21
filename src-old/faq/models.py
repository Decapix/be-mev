from django.db import models
import uuid

# Create your models here.


class Ask(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ask = models.TextField(max_length=360)
    description = models.TextField(max_length=4000)
    show = models.BooleanField()

    def __str__(self):
        return f"{self.ask}"
