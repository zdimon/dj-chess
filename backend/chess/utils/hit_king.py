from django.conf import settings
from .hit_figure import hit_figure, heal_figure
from .get_cell_id import get_cell_id

def hit_king(figure):
    from chess.models import Cell
    cell = Cell.objects.get(pk=figure.cellid)
    print('hitting from row %s col %s' % (cell.row,cell.col))
    hits = []

    
    
    tc = get_cell_id(figure.board,cell.row,cell.col+1)
    if tc:
        hits.append(tc)
    tc = get_cell_id(figure.board,cell.row+1,cell.col+1)
    if tc:
        hits.append(tc)
    tc = get_cell_id(figure.board,cell.row+1,cell.col)
    if tc:
        hits.append(tc)
    tc = get_cell_id(figure.board,cell.row+1,cell.col-1)
    if tc:
        hits.append(tc)
    tc = get_cell_id(figure.board,cell.row,cell.col-1)
    if tc:
        hits.append(tc)
    tc = get_cell_id(figure.board,cell.row-1,cell.col-1)
    if tc:
        hits.append(tc)
    tc = get_cell_id(figure.board,cell.row-1,cell.col)
    if tc:
        hits.append(tc)
    tc = get_cell_id(figure.board,cell.row-1,cell.col+1)
    if tc:
        hits.append(tc)
    

    print(hits)
    for c in hits:
        if(c.figure):
            if (c.figure.figure.color == figure.figure.color):
                heal_figure(c.figure,40)
            else:
                hit_figure(c.figure,40)
    