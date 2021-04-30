from django.core.management.base import BaseCommand
from chess.models import Figure
from django.core.files import File
from django.conf import settings
import os
from chess.models import UserProfile


FIGURES = [
    'pone',
    'king',
    'queen',
    'knite',
    'bishop',
    'rook'
]

class Command(BaseCommand):
    
    def handle(self, *args, **options):
        print('Loading figures')
        Figure.objects.all().delete()
        for fn in FIGURES:
            f = Figure()
            f.name = fn
            f.color = 'white'
            f.save()
            path = os.path.join(settings.BASE_DIR,'static','images',f'{fn}-white.svg')
            with open(path, 'rb') as doc_file:
                f.image.save(f'{fn}-white.svg', File(doc_file), save=True)
        for fn in FIGURES:
            f = Figure()
            f.name = fn
            f.color = 'black'
            f.save()
            path = os.path.join(settings.BASE_DIR,'static','images',f'{fn}-black.svg')
            with open(path, 'rb') as doc_file:
                f.image.save(f'{fn}-black.svg', File(doc_file), save=True)

        print('Loading users')
        UserProfile.objects.all().delete()
        for cnt in range(1,5):
            name = f't{cnt}'
            u = UserProfile()
            u.username = name
            u.set_password(name)
            u.publicname = name
            u.is_active = True
            u.is_superuser = True
            u.is_staff = True
            u.save()