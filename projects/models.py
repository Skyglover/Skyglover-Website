import calendar
from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone


class Project(models.Model):
    STATUS_CHOICES = (
        ('started', 'Started'),
        ('released', 'Released'),
    )

    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, default='', unique=True)
    status = models.CharField(max_length=15,
                              choices=STATUS_CHOICES,
                              default='started')
    start_date = models.DateTimeField(default=timezone.now)
    summary = models.TextField(max_length=500)
    description = models.TextField()

    class Meta:
        ordering = ('-start_date',)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.name)
        super().save(force_insert, force_update, using, update_fields)

    def get_start_date(self):
        return calendar.month_name[self.start_date.month] + ' ' + str(self.start_date.year)
