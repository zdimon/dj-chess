from django.conf import settings
from .hit_figure import hit_figure, heal_figure
from .get_cell_id import get_cell_id

def hit_queen(figure):
    from chess.models import Cell
    cell = Cell.objects.get(pk=figure.cellid)
    # print('hitting from row %s col %s' % (cell.row,cell.col))
    hits = []

    cnt = 1
    for c in range(cell.col,settings.BOARD_WIDTH+1):
        tc = get_cell_id(figure.board,cell.row+cnt,cell.col+cnt)
        if tc:
            hits.append(tc)
            if tc.figure:
                break
            cnt +=1
        else:
            break
    cnt = 1
    for c in range(cell.col,settings.BOARD_WIDTH+1):
        tc = get_cell_id(figure.board,cell.row+cnt,cell.col-cnt)
        if tc:
            hits.append(tc)
            if tc.figure:
                break
            cnt +=1
        else:
            break
        
    cnt = 1
    for c in range(cell.col,settings.BOARD_WIDTH+1):
        tc = get_cell_id(figure.board,cell.row-cnt,cell.col+cnt)
        if tc:
            hits.append(tc)
            if tc.figure:
                break
            cnt +=1
        else:
            break

    cnt = 1
    for c in range(cell.col,settings.BOARD_WIDTH+1):
        tc = get_cell_id(figure.board,cell.row-cnt,cell.col-cnt)
        if tc:
            hits.append(tc)
            if tc.figure:
                break
            cnt +=1
        else:
            break
    

    cnt = 1
    for c in range(cell.col,settings.BOARD_WIDTH+1):
        tc = get_cell_id(figure.board,cell.row,cell.col+cnt)
        if tc:
            hits.append(tc)
            if tc.figure:
                break
            cnt +=1
        else:
            break
    cnt = 1
    for c in range(cell.col,settings.BOARD_WIDTH+1):
        tc = get_cell_id(figure.board,cell.row+cnt,cell.col)
        if tc:
            hits.append(tc)
            if tc.figure:
                break
            cnt +=1
        else:
            break
        
    cnt = 1
    for c in range(cell.col,settings.BOARD_WIDTH+1):
        tc = get_cell_id(figure.board,cell.row,cell.col-cnt)
        if tc:
            hits.append(tc)
            if tc.figure:
                break
            cnt +=1
        else:
            break

    cnt = 1
    for c in range(cell.col,settings.BOARD_WIDTH+1):
        tc = get_cell_id(figure.board,cell.row-cnt,cell.col)
        if tc:
            hits.append(tc)
            if tc.figure:
                break
            cnt +=1
        else:
            break



    print(hits)
    for c in hits:
        if(c.figure):
            if (c.figure.figure.color == figure.figure.color):
                heal_figure(c.figure,20)
            else:
                hit_figure(c.figure,20)
    