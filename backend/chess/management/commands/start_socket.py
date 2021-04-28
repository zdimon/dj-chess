from django.core.management.base import BaseCommand, CommandError
import threading
import socketio
import eventlet
eventlet.monkey_patch()
mgr = socketio.RedisManager('redis://localhost:6379/0')
sio = socketio.Server(cors_allowed_origins='*',async_mode='eventlet',client_manager=mgr)

app = socketio.WSGIApp(sio)

@sio.event
def connect(sid, environ):
    print('connect ', sid)


@sio.event
def disconnect(sid):
    print('disconnect ', sid)
    thread = threading.Thread(target=remove_user_task, args=(sid,))
    thread.start()

class Command(BaseCommand):
    
    def handle(self, *args, **options):
        print('Statrting socket server')
        eventlet.wsgi.server(eventlet.listen(('', 5001)), app)

        