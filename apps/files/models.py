from django.db import models
from django.contrib.auth.models import User
from courses.models import Course
from django.core.urlresolvers import reverse
from django.utils.text import slugify
import json, os

class Category(models.Model):
    name = models.CharField(max_length=100)

    @property
    def slug(self):
        return slugify(self.name)

    def __str__(self):
        return self.name


class File(models.Model):
    user = models.ForeignKey(User)
    course = models.ForeignKey(Course)
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=100)
    file = models.FileField()
    created_on = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('files.views.details', args=(self.pk,))

    def to_json(self):
        return json.dumps({
            'user': {
                'id': self.user.id,
                'name': self.user.username
            },
            'title': self.title,
            'file': {
                'name': os.path.basename(self.file.path),
                'url': self.file.url
            }}, indent=2)

    def __str__(self):
        return '{}:{}'.format(self.course, self.title)
