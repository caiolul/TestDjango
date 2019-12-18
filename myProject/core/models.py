from django.db import models


class Quest (models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
# Create your models here.

