from django.db import models
from django.utils import timezone


class Post():
    author = models.ForeignKey('auth.User')

    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
