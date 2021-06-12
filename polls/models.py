import datetime

from django.db import models
from django.utils import timezone
from django.contrib import auth
from django.contrib.postgres.fields import ArrayField
from django import forms

User = auth.get_user_model()

class Question(models.Model):
    question_text = models.CharField(max_length=50, default="Question text")
    pub_date = models.DateTimeField(auto_now=True, null=True)
    choice_one = models.CharField(max_length=50, default="choice one")
    choice_two = models.CharField(max_length=50, default="choice two")
    choice_three = models.CharField(max_length=50, default="choice three")
    votes_one = models.IntegerField(default=0)
    votes_two = models.IntegerField(default=0)
    votes_three = models.IntegerField(default=0)
    pollcreator = models.CharField(max_length=50, default="NoCreator")
    
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Vote(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #choice = models.ForeignKey(Choice, on_delete=models.CASCADE, default="NO_CHOICE")

class CreatePollForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text', 'choice_one', 'choice_two', 'choice_three']