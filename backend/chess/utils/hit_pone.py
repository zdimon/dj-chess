from django.conf import settings
from .hit_figure import hit_figure
from .get_cell_id import get_cell_id

def hit_pone(figure):
    from chess.models import Cell
    cell = Cell.objects.get(pk=figure.cellid)
    print('hitting from row %s col %s' % (cell.row,cell.col))
    hits = []
    if figure.figure.color == 'white':
        if(cell.col == 1):
            hits.append(get_cell_id(figure.board,cell.row+1,cell.col+1))

        elif(cell.col == settings.BOARD_WIDTH):
            hits.append(get_cell_id(figure.board,cell.row+1,cell.col-1))

        else:
            hits.append(get_cell_id(figure.board,cell.row+1,cell.col+1))
            hits.append(get_cell_id(figure.board,cell.row+1,cell.col-1))

    if figure.figure.color == 'black':
        if(cell.col == 1):
            hits.append(get_cell_id(figure.board,cell.row-1,cell.col-1))

        elif(cell.col == settings.BOARD_WIDTH):
            hits.append(get_cell_id(figure.board,cell.row-1,cell.col+1))

        else:
            hits.append(get_cell_id(figure.board,cell.row-1,cell.col-1))
            hits.append(get_cell_id(figure.board,cell.row-1,cell.col+1))

    print(hits)
    for c in hits:
        if(c.figure):
            hit_figure(c.figure)

