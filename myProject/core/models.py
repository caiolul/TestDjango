import datetime
from django.conf import settings
from django.db import models
from django.utils import timezone


class Post (models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    description = models.TextField()    
    created_date = models.DateTimeField(default=timezone.now)
    pub_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

    def pub(self):
        self.pub_date = timezone.now()
        self.save()

class Login (models.Model):
    email = models.EmailField(max_length=260)
    #passwd = models.CharField(max_length=50)
    passwd = models.TextField()

