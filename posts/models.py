from django.db import models
from datetime import datetime

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    create_At = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "Posts"
