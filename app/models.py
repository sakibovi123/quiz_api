from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Type(models.Model):
    type_name = models.CharField(max_length=255)

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.type_name


class Category(models.Model):
    category_name = models.CharField(max_length=255)

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.category_name


class Answer(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.title


class Quiz(models.Model):
    created_at = models.DateTimeField(default=datetime.today)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, null=True, blank=True)
    quiz_title = models.CharField(max_length=255)
    options = models.ManyToManyField(Answer, blank=True, related_name="options")
    correct_answer = models.ManyToManyField(Answer, blank=True, related_name="correct_answer")
    is_correct = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.quiz_title


class Submit(models.Model):
    submission_time = models.DateTimeField(default=datetime.today())
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    answers = models.ManyToManyField(Answer, blank=True)