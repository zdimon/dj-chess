from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from django.conf import settings
from chess.serializers import BoardSerializer
from chess.models import User2Figure, Board

class GamesView(APIView):
    '''
    Get game list.

    _______________________

    '''
    
    permission_classes = (IsAuthenticated,)
    @swagger_auto_schema( 
        
    )
    def get(self, request, format=None):
        boards = []
        for b in Board.objects.all():
            try:
                agressor = b.agressor.username
            except:
                agressor = None
            boards.append({"id": b.uuid, "owner": b.owner.username, "agressor": agressor})
        return Response(boards)

