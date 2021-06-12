from django.db import models
from django.contrib import auth
from django import forms

User = auth.get_user_model()

class Post(models.Model):
    title = models.CharField(max_length=100, default="BlogPost Title")
    date = models.DateTimeField(auto_now_add=True)
    #author = models.ForeignKey(User, on_delete= models.CASCADE, related_name='blog_posts')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(default="BlogPost Body")
 
    def __str__(self):
        return self.title


class CreatePollForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body']
