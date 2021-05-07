from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated
from chess.serializers import BoardSerializer, CellSerializer
from chess.utils import get_or_create_board
from chess.models import Board, Cell, User2Figure
import json
from chess.utils import give_figures, load_classic_board
from chess.tasks import update_board

class LoadClassicBoardView(APIView):
    '''
    Set figure on desk in classic way. 

    _______________________

    '''
    
    permission_classes = (IsAuthenticated,)
    @swagger_auto_schema( 
        responses={200: BoardSerializer }
        )
    def get(self, request, board_id, format=None):
        board = Board.objects.get(uuid=board_id)
        load_classic_board(board, request.user.userprofile)
        update_board.delay(board_id)
        return Response({"status": 0, "message": "Ok"})

