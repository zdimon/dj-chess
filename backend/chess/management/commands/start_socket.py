from django.core.management.base import BaseCommand, CommandError
import threading
import socketio
import eventlet
from chess.models import UserProfile
eventlet.monkey_patch()
from django.conf import settings
mgr = socketio.RedisManager(settings.SOCKET_BROKER_URL)
sio = socketio.Server(cors_allowed_origins='*',async_mode='eventlet',client_manager=mgr)
app = socketio.WSGIApp(sio)

def add_user_sid(sid,data):
    try:
        user = UserProfile.objects.get(username=data['login'])
        user.add_sid(sid)
    except Exception as e:
        print(e)
        print(data['login'])

def remove_user_sid(sid):
    UserProfile.remove_sid(sid)

@sio.event
def login(sid, data):
    print('Adding sid %s' % sid)
    print(data)
    thread = threading.Thread(target=add_user_sid, args=(sid,data))
    thread.start()


@sio.event
def connect(sid, environ):
    print('connect ', sid)

@sio.event
def disconnect(sid):
    print('disconnect ', sid)
    thread = threading.Thread(target=remove_user_sid, args=(sid,))
    thread.start()


@sio.event
def disconnect(sid):
    print('disconnect ', sid)
    thread = threading.Thread(target=remove_user_sid, args=(sid,))
    thread.start()

class Command(BaseCommand):
    
    def handle(self, *args, **options):
        print('Statrting socket server')
        eventlet.wsgi.server(eventlet.listen(('', 5001)), app)

        