from django.db import models
from django.utils import timezone
from django.contrib import admin


import datetime


class Question(models.Model):
    # Class variables are defined below (a text field and a datetime field)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    # The __str__ function will format the model to be more readable when interacting with the API
    def __str__(self):
        return self.question_text

    # Ensures the question was published recently by ensuring the user-entered "pub_date" is more recent than yesterday
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?',
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # CharField is required to have a max_length arg
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
