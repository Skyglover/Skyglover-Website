from django.db import models
from django.template.defaultfilters import slugify


class Project(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, default='')
    description = models.CharField(max_length=500)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.name)
        super().save(force_insert, force_update, using, update_fields)
