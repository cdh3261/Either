from django.db import models

# Create your models here.

class Question(models.Model):
    title = models.CharField(max_length=100)
    option_a = models.CharField(max_length=100)
    option_b = models.CharField(max_length=100)
    img_a = models.TextField()
    img_b = models.TextField()

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    comment = models.CharField(max_length=300)
    username = models.CharField(max_length=50)
    comment_date = models.DateField()
    pick = models.IntegerField()