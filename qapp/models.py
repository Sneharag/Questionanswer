from django.db import models

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    phone=models.CharField(max_length=10,unique=True)

class Question(models.Model):

    title = models.CharField(max_length=200)

    description = models.TextField(null=True)

    image = models.ImageField(upload_to="questions/images/", null=True, blank=True)

    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return self.title


class Answer(models.Model):

    comment = models.TextField()

    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    question_object = models.ForeignKey(Question, on_delete=models.CASCADE)

    up_vote = models.ManyToManyField(User, blank=True)

    down_vote = models.ManyToManyField(User, blank=True)

   

