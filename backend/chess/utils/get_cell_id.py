from django.conf import settings
from chess.models import Cell
def get_cell_id(board, row, col):
    print('geting cell %s %s' % (row, col))
    try:
        cell = Cell.objects.get(board=board,row=row,col=col)
        return cell
    except:
        return False