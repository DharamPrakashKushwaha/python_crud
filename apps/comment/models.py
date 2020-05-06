from datetime import timezone

from django.contrib.auth.models import User
from django.db import models
from apps.blog.models import Post


# Create your models here.

class Comment(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE, null=False)
    comment = models.TextField(default='')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    createdAt = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.comment
