from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from files.models import File
from courses.models import Course
from django.utils.dateparse import parse_date
import os, json, random
from django.db import IntegrityError
from os.path import join
BASE_DIR = os.path.dirname(__file__)

class Command(BaseCommand):

    def handle(self, *args, **options):
        File.objects.all().delete()
        files = json.load(open(join(BASE_DIR, 'files.json')))
        for f in files:
            course = Course.objects.get(name=f.get('course'))
            user = self.get_or_create_user(f.get('author'))
            date = parse_date(f.get('date')) 
            file_inst = File(pk=f.get('id'), title=f.get('title'),
                    course=course, created_on=date, user=user, url=f.get('download_link')) 
            file_inst.save()

    def get_or_create_user(self, username):
        try:
            password = ''.join(random.sample("qwertyuiop[asdfghjkl;zxcvbnm,",20))
            return User.objects.create_user(username, username+'@etu.utc.fr', password)
        except IntegrityError:
            return User.objects.get(username=username)
