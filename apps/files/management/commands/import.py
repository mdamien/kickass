from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from files.models import File
from courses.models import Course
import os, json, random
from django.db import IntegrityError
from os.path import join
import datetime
BASE_DIR = os.path.dirname(__file__)

class Command(BaseCommand):

    def handle(self, *args, **options):
        File.objects.all().delete()
        files = json.load(open(join(BASE_DIR, 'files.json')))
        for f in files:
            course = Course.objects.get(name=f.get('course'))
            user = self.get_or_create_user(f.get('author'))
            date = datetime.datetime.strptime(f.get('date'), "%d/%m/%Y").date()
            file_inst = File(pk=f.get('id'), title=f.get('title'),
                    course=course, user=user, url=f.get('download_link')) 
            file_inst.save()
            file_inst.created_on = date
            file_inst.save()

    def get_or_create_user(self, username):
        try:
            password = ''.join(random.sample("qwertyuiop[asdfghjkl;zxcvbnm,",20))
            return User.objects.create_user(username, username+'@etu.utc.fr', password)
        except IntegrityError:
            return User.objects.get(username=username)
