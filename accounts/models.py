from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass


class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    caption = models.CharField(max_length=255)
    users = models.ManyToManyField(User, related_name='images')

    def __str__(self):
        return self.caption
    
class Comment(models.Model):
    photo = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    posted_at = models.DateTimeField(auto_now_add=True)