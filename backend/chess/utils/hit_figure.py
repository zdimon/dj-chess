from django.conf import settings
from chess.models import Cell

def hit_figure(figure,damage=10):
    print('damage to %s' % figure.figure)
    figure.helth -= damage
    figure.save()
    