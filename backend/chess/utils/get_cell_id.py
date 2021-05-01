from django.conf import settings
from chess.models import Cell
def get_cell_id(board, row, col):
    print('geting cell')
    cell = Cell.objects.get(board=board,row=row,col=col)
    return cell