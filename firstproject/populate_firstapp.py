import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','firstproject.settings')

import django
django.setup()


import random
from firstapp.models import Topic,Webpage,AccessRecord,users
from faker import Faker

fakegen = Faker()

topics = ['Search', 'Social', 'Marketplace', 'News','Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):

    for entry in range(N):

        top = add_topic()

        fakeurl = fakegen.url()
        fakedate = fakegen.date()
        fakename = fakegen.company()
        fakename = fakegen.name().split()
        fakefname = fakename[0]
        fakelname = fakename[1]
        fakeemail = fakegen.email()

        w = Webpage.objects.get_or_create(topic=top,url=fakeurl,name=fakename)[0]
        a = AccessRecord.objects.get_or_create(name=w,date=fakedate)[0]
        u = users.objects.get_or_create(fname=fakefname,lname=fakelname,email=fakeemail)

if __name__ == '__main__':
    print("Populating Script!!!!!")
    populate(5)
    print("Populating Complete!!")
