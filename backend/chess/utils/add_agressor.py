
def add_agressor(board, user):
    board.agressor = user
    board.save()
    return board
    