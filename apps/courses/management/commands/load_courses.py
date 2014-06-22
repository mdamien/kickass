from django.core.management.base import BaseCommand, CommandError
from courses.models import Course
from files.models import File
import json
import os
from os.path import join
BASE_DIR = os.path.dirname(__file__)

class Command(BaseCommand):
    def handle(self, *args, **options):
        Course.objects.all().delete()
        uvs = json.load(open(join(BASE_DIR, 'uvs.json')))
        for uv in uvs:
            Course(name=uv.get('name'), descr=uv.get('title')).save()
