from django.db import models


class Member(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=100)
    information = models.TextField()

    class Meta:
        ordering = ('id',)
