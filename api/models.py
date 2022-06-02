from django.db import models
from uuid import uuid4
# Create your models here.


class Record(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    email = models.EmailField(unique=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ['name']
