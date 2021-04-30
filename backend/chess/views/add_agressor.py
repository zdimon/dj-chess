from chess.models import Board
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated
from chess.serializers import BoardSerializer
from chess.utils import add_agressor

class AddAgressorBoardView(APIView):
    '''
    Add a rival.

    _______________________

    '''
    
    permission_classes = (IsAuthenticated,)
    @swagger_auto_schema( 
        responses={200: BoardSerializer }
        )
    def get(self, request, board_id, format=None):
        board = Board.objects.get(uuid=board_id)
        return Response(BoardSerializer(add_agressor(board,request.user.userprofile)).data)
