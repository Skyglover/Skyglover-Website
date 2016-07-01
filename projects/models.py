from django.db import models
from django.template.defaultfilters import slugify


class Project(models.Model):
    STATUS_CHOICES = (
        ('started', 'Started'),
        ('released', 'Released'),
    )

    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, default='', unique=True)
    description = models.CharField(max_length=500)
    status = models.CharField(max_length=15,
                              choices=STATUS_CHOICES,
                              default='started')

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.name)
        super().save(force_insert, force_update, using, update_fields)
