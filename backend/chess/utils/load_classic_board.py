from chess.models import Figure, User2Figure, Cell

def load_classic_board(board, user):
    pones = User2Figure.objects.filter(board=board,user=user,figure__name='pone',on_board=False)
    cnt = 0
    for f in pones:
        if f.figure.color == 'white':
            trow1 = 2
            trow2 = 1
        else:
            trow1 = 7
            trow2 = 8
        cnt +=1
        cell = Cell.objects.get(board=board,row=trow1, col=cnt)
        cell.figure = f
        cell.save()
        f.on_board = True
        f.save()

    rooks = User2Figure.objects.filter(board=board,user=user,figure__name='rook',on_board=False)

    cell = Cell.objects.get(board=board,row=trow2, col=1)
    cell.figure = rooks[0]
    cell.save()
    cell = Cell.objects.get(board=board,row=trow2, col=8)
    cell.figure = rooks[1]
    cell.save()
    for f in rooks:
        f.on_board = True
        f.save()

    knites = User2Figure.objects.filter(board=board,user=user,figure__name='knite',on_board=False)
    cell = Cell.objects.get(board=board,row=trow2, col=2)
    cell.figure = knites[0]
    cell.save()
    cell = Cell.objects.get(board=board,row=trow2, col=7)
    cell.figure = knites[1]
    cell.save()
    for f in knites:
        f.on_board = True
        f.save()

    bishops = User2Figure.objects.filter(board=board,user=user,figure__name='bishop',on_board=False)
    cell = Cell.objects.get(board=board,row=trow2, col=3)
    cell.figure = bishops[0]
    cell.save()
    cell = Cell.objects.get(board=board,row=trow2, col=6)
    cell.figure = bishops[1]
    cell.save()
    for f in bishops:
        f.on_board = True
        f.save()

    king = User2Figure.objects.get(board=board,user=user,figure__name='king',on_board=False)
    cell = Cell.objects.get(board=board,row=trow2, col=4)
    cell.figure = king
    cell.save()
    king.on_board = True
    king.save()

    queen = User2Figure.objects.get(board=board,user=user,figure__name='queen',on_board=False)
    cell = Cell.objects.get(board=board,row=trow2, col=5)
    cell.figure = queen
    cell.save()
    queen.on_board = True
    queen.save()
    if board.owner == user:
        board.owner_position_done = True
    if board.agressor == user:
        board.agressor_position_done = True
    board.save()
    return board
    