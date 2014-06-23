from django.db import models

class Course(models.Model):
    name = models.SlugField()
    descr = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)

