from django.core.management.base import BaseCommand
from chess.tasks import update_users_online

class Command(BaseCommand):
    
    def handle(self, *args, **options):
        print('Testing_online')
        update_users_online.delay()

        