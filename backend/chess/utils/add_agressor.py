from chess.utils.create_board import give_figures

def add_agressor(board, user):
    board.agressor = user
    board.save()
    give_figures(board,user,"black")
    return board
    