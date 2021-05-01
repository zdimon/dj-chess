from django.conf import settings
from chess.models import Cell

def hit_figure(figure,damage=10):
    print('damage to %s' % figure.figure)
    if figure.helth > 0:
        figure.helth -= damage
        if figure.helth < 0:
            figure.helth = 0
        figure.save()
    if figure.helth == 0:
        figure.delete()
    
def heal_figure(figure,damage=10):
    print('damage to %s' % figure.figure)
    if figure.helth < 100:
        figure.helth += damage
        figure.save()