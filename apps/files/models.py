from django.db import models
from django.contrib.auth.models import User
from courses.models import Course
from django.core.urlresolvers import reverse
from django.utils.text import slugify
import json, os

class File(models.Model):
    user = models.ForeignKey(User)
    course = models.ForeignKey(Course)
    title = models.CharField(max_length=100)
    file = models.FileField()
    created_on = models.DateField(auto_now_add=True)
    hidden = models.BooleanField(default=False) #admin-only

    url = models.URLField(blank=True, null=True) #TODO download everything

    def download_url(self):
        return self.file.url if self.file else self.url

    def get_absolute_url(self):
        return reverse('files.views.details', args=(self.pk,))

    def __str__(self):
        return '{}:{}'.format(self.course, self.title)

    class Meta:
        ordering = ('course', 'created_on')

