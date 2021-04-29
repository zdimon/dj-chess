import socketio
from celery import shared_task
from django.conf import settings
mgr = socketio.RedisManager(settings.CELERY_BROKER_URL, write_only=True)


@shared_task
def update_users_online():
    from .models import UserProfile
    print('Sending update online command!')
    for user in UserProfile.objects.filter(is_online=True):
        for room in user.get_sids():
            mgr.emit('update_online_user', data={"message": "do update!"}, room=room)
