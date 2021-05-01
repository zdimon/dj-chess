from rest_framework import serializers
from chess.models import Board, Cell
from .cell_serializer import CellSerializer


class BoardSerializer(serializers.ModelSerializer):
    cells = serializers.SerializerMethodField()

    def __init__(self, *args, **kwargs):
        try:
            self.user = kwargs.pop('user')
        except:
            pass
        super().__init__(*args, **kwargs)

    def get_cells(self, obj=None):
        cells = []
        try:
            if self.user.username != obj.owner.username:
                cells_q =  Cell.objects.filter(board=obj).order_by('id')
            else:
                cells_q =  Cell.objects.filter(board=obj).order_by('-id')
        except:
            cells_q =  Cell.objects.filter(board=obj).order_by('-id')
        for c in cells_q:
            cells.append(CellSerializer(c).data)
        return cells

    class Meta:
        model = Board
        fields = [   
                    'owner', 
                    'agressor',
                    'uuid',
                    'cells',
                    'stage'
                    ]


