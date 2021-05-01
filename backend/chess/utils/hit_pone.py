from django.conf import settings
from .hit_figure import hit_figure
from .get_cell_id import get_cell_id

def hit_pone(figure):
    from chess.models import Cell
    cell = Cell.objects.get(pk=figure.cellid)
    # print('hitting from row %s col %s' % (cell.row,cell.col))
    hits = []
    if figure.figure.color == 'white':
        if(cell.col == 1):
            tc = get_cell_id(figure.board,cell.row+1,cell.col+1)
            if tc:
                hits.append(tc)

        elif(cell.col == settings.BOARD_WIDTH):
            tc = get_cell_id(figure.board,cell.row+1,cell.col-1)
            if tc:
                hits.append(tc)

        else:
            tc = get_cell_id(figure.board,cell.row+1,cell.col+1)
            if tc:
                hits.append(tc)
            tc = get_cell_id(figure.board,cell.row+1,cell.col-1)
            if tc:
                hits.append(tc)

    if figure.figure.color == 'black':
        if(cell.col == 1):
            tc = get_cell_id(figure.board,cell.row-1,cell.col-1)
            if tc:
                hits.append(tc)

        elif(cell.col == settings.BOARD_WIDTH):
            tc = get_cell_id(figure.board,cell.row-1,cell.col+1)
            if tc:
                hits.append(tc)

        else:
            tc = get_cell_id(figure.board,cell.row-1,cell.col-1)
            if tc:
                hits.append(tc)
            tc = get_cell_id(figure.board,cell.row-1,cell.col+1)
            if tc:
                hits.append(tc)

    for c in hits:
        if(c.figure):
            if (c.figure.figure.color == figure.figure.color):
                heal_figure(c.figure,20)
            else:
                hit_figure(c.figure,20)

