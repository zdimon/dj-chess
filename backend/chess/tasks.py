import socketio
from celery import shared_task
from django.conf import settings
mgr = socketio.RedisManager(settings.SOCKET_BROKER_URL, write_only=True)
import json

@shared_task
def update_users_online():
    from .models import UserProfile
    print('Sending update online command!')
    for user in UserProfile.objects.filter(is_online=True):
        for room in user.get_sids():
            print(room)
            mgr.emit('update_online_user', data={"message": "do update!"}, room=room)


@shared_task
def update_board(board_id):
    from .models import Board
    from chess.serializers import BoardSerializer
    board = Board.objects.get(pk=board_id)
    print('Sending update board command!')
    try:
        for room in board.agressor.get_sids():
            print(room)
            mgr.emit('update_board', data=BoardSerializer(board,user=board.agressor).data, room=room)
    except:
        print('No agressor')
    for room in board.owner.get_sids():
        print(room)
        mgr.emit('update_board', data=BoardSerializer(board,user=board.owner).data, room=room)

@shared_task
def control_stage(board_id):
    print('Controlling stage')
    from .models import Board, User2Figure
    board = Board.objects.get(pk=board_id)
    if User2Figure.objects.filter(board=board,on_board=False).count() == 0:
        board.stage = 'play'
        board.owner_position_done = True
        board.agressor_position_done = True
        board.save()
        for room in board.agressor.get_sids():
            print(room)
            mgr.emit('update_stage', data={"stage": "play"}, room=room)
        for room in board.owner.get_sids():
            print(room)
            mgr.emit('update_stage', data={"stage": "play"}, room=room)

@shared_task
def hit_figures(board_id,user_id):
    from .models import Board, User2Figure
    from chess.utils import hit_pone, hit_bishop, hit_rook, hit_queen, hit_knite, hit_king
    board = Board.objects.get(pk=board_id)
    figures = User2Figure.objects.filter(board=board,user_id=user_id)
    for figure in figures:
        print(figure)
        if figure.figure.name == 'pone':
            hit_pone(figure)
        if figure.figure.name == 'bishop':
            hit_bishop(figure)
        if figure.figure.name == 'rook':
            hit_rook(figure)
        if figure.figure.name == 'queen':
            hit_queen(figure)
        if figure.figure.name == 'knite':
            hit_knite(figure)
        if figure.figure.name == 'king':
            hit_king(figure)
    update_board.delay(board.uuid)


@shared_task
def hit_figure(figure_id):
    from .models import Board, User2Figure
    from chess.utils import hit_pone, hit_bishop, hit_rook, hit_queen, hit_knite, hit_king
    figure = User2Figure.objects.get(pk=figure_id)
    board = figure.board
    if figure.figure.name == 'pone':
        hit_pone(figure)
    if figure.figure.name == 'bishop':
        hit_bishop(figure)
    if figure.figure.name == 'rook':
        hit_rook(figure)
    if figure.figure.name == 'queen':
        hit_queen(figure)
    if figure.figure.name == 'knite':
        hit_knite(figure)
    if figure.figure.name == 'king':
        hit_king(figure)

    update_board.delay(board.uuid)