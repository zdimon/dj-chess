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
    for room in board.agressor.get_sids():
        print(room)
        mgr.emit('update_board', data=BoardSerializer(board,user=board.agressor).data, room=room)
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
        board.save()
        for room in board.agressor.get_sids():
            print(room)
            mgr.emit('update_stage', data={"stage": "play"}, room=room)
        for room in board.owner.get_sids():
            print(room)
            mgr.emit('update_stage', data={"stage": "play"}, room=room)