from django.db import models


class SomeText(models.Model):
    identifier = models.CharField(max_length=100, db_index=True)
    text = models.TextField()

    class Meta:
        ordering = ('identifier',)
