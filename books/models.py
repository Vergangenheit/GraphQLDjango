from django.db import models
from django.db.models import CharField


# Create your models here.
class Books(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.TextField()

    def __str__(self) -> CharField:
        return self.title
