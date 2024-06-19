from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # alternative (it'll update the date & time when an object is created)
    # date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
