from django.db import models
from django.contrib.auth.models import User


class Poll(models.Model):
    question = models.CharField(max_length=200)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    publish_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question


class Choice(models.Model):
    poll = models.ForeignKey(Poll, related_name="choices", on_delete=models.CASCADE)
    text = models.CharField(max_length=100)

    def __str__(self):
        return self.text


class Vote(models.Model):
    poll = models.ForeignKey(Poll, related_name="votes", on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, related_name="votes", on_delete=models.CASCADE)
    voted_by = models.ForeignKey(User, related_name="votes", on_delete=models.CASCADE)

    class Meta:
        unique_together = ("poll", "voted_by")
