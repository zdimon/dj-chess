from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated
from chess.serializers import BoardSerializer, CellSerializer
from chess.utils import get_or_create_board
from chess.models import Board, Cell, User2Figure
import json
from chess.tasks import update_board


class SetFigureView(APIView):
    '''
    Set figure on desk.

    _______________________

    '''
    
    permission_classes = (IsAuthenticated,)
    @swagger_auto_schema( 
        responses={200: BoardSerializer }
        )
    def post(self, request, format=None):
        # cells = []
        data = json.loads(request.body)
        board = Board.objects.get(uuid=data["uuid"])
        print(board)
        u2f = User2Figure.objects.get(id=data["figure"])
        cell = Cell.objects.get(id=data["cell"])
        u2f.on_board = True
        u2f.save()
        cell.figure = u2f
        cell.save()
        # for c in Cell.objects.filter(board=board):
        #     cells.append(CellSerializer(c))
        # print(cells)
        # board.cells = cells
        update_board.delay(board.uuid)
        return Response(BoardSerializer(board).data)

