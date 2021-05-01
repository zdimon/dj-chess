from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from django.conf import settings
from chess.serializers import FigureSerializer
from chess.models import User2Figure

class GetFiguresView(APIView):
    '''
    Get figures.

    _______________________

    '''
    
    permission_classes = (IsAuthenticated,)
    @swagger_auto_schema( 
        
    )
    def get(self, request, format=None):
        print(request.user)
        figures = []
        for f in User2Figure.objects.filter(user=request.user,on_board=False):
            figures.append(FigureSerializer(f).data)
        return Response(figures)

