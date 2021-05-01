from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated
from chess.serializers import BoardSerializer, CellSerializer
from chess.utils import get_or_create_board
from chess.models import Board, Cell, User2Figure
import json
from chess.tasks import update_board, control_stage


class MoveFigureView(APIView):
    '''
    Move figure on desk.

    _______________________

    '''
    
    permission_classes = (IsAuthenticated,)
    @swagger_auto_schema( 
        responses={200: BoardSerializer }
        )
    def post(self, request, format=None):
        data = json.loads(request.body)
        board = Board.objects.get(pk=data["board"])
        cell_from = Cell.objects.get(pk=data["from"])
        cell_to = Cell.objects.get(pk=data["to"])
        cell_to.figure = cell_from.figure
        cell_from.figure = None
        cell_from.save()
        cell_to.save()
        update_board.delay(board.uuid)
        return Response({"status": 0, "message": "Ok"})

