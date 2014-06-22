from django.db import models

class Course(models.Model):
    name = models.SlugField()

    def __str__(self):
        return self.name

