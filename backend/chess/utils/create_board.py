from chess.models import Board, Figure, User2Figure, Cell

def make_cells(board):
    for x_item in range(1,9):
        tmp = [*range(1,9)]
        for t in tmp:
            c = Cell()
            c.board = board
            if x_item%2 == 0:
                if t%2 == 0 :
                    c.color = 'black'
                else:
                    c.color = 'white'
            else:
                if t%2 == 0 :
                    c.color = 'white'
                else:
                    c.color = 'black'
            c.save()
            


def give_figures(board,user,color="white"):
    for f in Figure.objects.filter(color=color):
        if f.name == 'pone':
            for cnt in range(1,9):
                u2f = User2Figure()
                u2f.figure = f
                u2f.user = user
                u2f.board = board
                u2f.save()
        elif f.name == 'rook' or f.name == 'bishop' or f.name == 'knite':
            for cnt in range(1,3):
                u2f = User2Figure()
                u2f.figure = f
                u2f.user = user
                u2f.board = board
                u2f.save()
        else:
            u2f = User2Figure()
            u2f.figure = f
            u2f.user = user
            u2f.board = board
            u2f.save()


def get_or_create_board(user):
    print('Creating board!')
    try:
        board = Board.objects.get(owner=user)
    except:
        board = Board()
        board.owner = user
        board.save()
        give_figures(board,board.owner)
        make_cells(board)
    return board