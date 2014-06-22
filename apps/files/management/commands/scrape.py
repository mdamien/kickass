from django.core.management.base import BaseCommand, CommandError

import json
import requests
from bs4 import BeautifulSoup 

import os, sys
from os.path import join
BASE_DIR = os.path.dirname(__file__)

class Command(BaseCommand):
    def handle(self, *args, **options):
        all_files = []
        for course in UVS:
            print(course)
            resp = requests.post('http://www.shwet.fr/rechercher.php', 
                    data={'search':course})
            soup = BeautifulSoup(resp.text)
            files = soup.find_all('tr')[1:]
            print(len(files),'files')
            for file in files:
                id = file.find(class_='titre').find('a').get('href').split('=')[-1]
                download_link = 'http://www.shwet.fr/dl.php?id='+id
                resp = requests.head(download_link, allow_redirects=False)
                try:
                    download_link = resp.headers['Location']
                except:
                    print(file)
                scrapped = {
                    'title': file.find(class_='titre').find('a').text,
                    'author': file.find(class_='tableau_auteur').find('a').text,
                    'date': file.find(class_='tableau_date').text,
                    'category': file.find(class_='categorie').find('a').text,
                    'course': file.find(class_='matiere').find('a').text,
                    'mark': file.find(class_='note').text,
                    'downloads': file.find(class_='compteur').text,
                    'download_link': download_link,
                    'id':int(id),
                }
                print('    ',scrapped.get('title'))
                all_files.append(scrapped)
            with open(join(BASE_DIR, 'files.tmp.json'),'w') as f:
                json.dump(all_files, f,  indent=2)


#copy-paste of the 'available UVs' list
UVS = """
  BL01 BL10   BL20   BL22   BL30   BT09   BT21   C2I1   CM01   CM11   CM12   CM13   CM15   FQ01   GE10   GE12   GE15   GE20 GE21   GE22   GE28   GE36   GE37   GE40   GE90   HE03   HE05   IA01   IA02   IC01   IC03   IR01   LA12   LA13   LA14   LA23
      LB14   LC14   LG30   LO01   LO21   LO22   MI01   MI03   MQ02   MQ03   MQ04   MT09   MT10   MT12   MT22   MT23   MT90   MT91
        MT94   NF01   NF04   NF11   NF16   NF17   NF29   NF92   NF93   NP90   PH02   PH09   PS04   PS09   PS91   PS92   PS93   PS94
          RO03   SC01   SC11   SC21   SC22   SC24   SI05   SI28   SO04   SP01   SR02   SY01   SY05   SY06   SY08   SY10   TF01   TN01
            TN03   TN04   TN05   TN06   TN07   TN09   TN12   TN18   TR91   UR02
""".split()
