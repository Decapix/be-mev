from django.db import models
import uuid

# Create your models here.



class Client(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    identification_number = models.CharField(max_length=6, unique=True, default='123456')

    def __str__(self):
        return self.identification_number
