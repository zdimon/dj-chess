from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from drf_yasg.utils import swagger_auto_schema
from django.conf import settings
import os
import json

class GetBoardView(APIView):
    '''
    Get board.

    _______________________

    '''
    
    permission_classes = ()
    authentication_classes = ()
    @swagger_auto_schema( 
        
        )
    def get(self, request, format=None):
        path = os.path.join(settings.BASE_DIR,'static', 'db.json')
        with open(path, 'r') as f:
            dt = json.loads(f.read())
        return Response(dt)

