from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from django.conf import settings
from chess.models import Board
from chess.serializers import BoardSerializer


class GetBoardView(APIView):
    '''
    Get board.

    _______________________

    '''
    
    permission_classes = (IsAuthenticated,)
    @swagger_auto_schema( 
            responses={200: BoardSerializer }
        )
    def get(self, request, board_id, format=None):
        board = Board.objects.get(uuid=board_id)
        return Response(BoardSerializer(board, user=self.request.user).data)

