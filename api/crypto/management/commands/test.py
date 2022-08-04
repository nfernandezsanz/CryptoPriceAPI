# -*- encoding: utf-8 -*-
from django.core.management.base import BaseCommand
from django.utils                import timezone 

class Command(BaseCommand):
    help = u'Prueba Cron'

    def handle(self, *args, **options):
        f= open("cron.txt","w+")
        f.write(str(timezone.now()))

        

