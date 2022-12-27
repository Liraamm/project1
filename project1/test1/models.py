from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=40)
    description = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

