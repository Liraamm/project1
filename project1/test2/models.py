from django.db import models

class Comment(models.Model):
    username = models.CharField(max_length=20)
    descript = models.TextField()
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'comment by user: {self.username}'