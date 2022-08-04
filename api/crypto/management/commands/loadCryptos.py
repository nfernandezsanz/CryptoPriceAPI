# -*- encoding: utf-8 -*-
from django.core.management.base import BaseCommand
from django.utils import timezone 
from crypto.viewsets import load_cryptos
class Command(BaseCommand):
    help = u'Prueba Cron'

    def handle(self, *args, **options):
        load_cryptos()

        

