from rest_framework import serializers
from chess.models import Board, Cell
from .cell_serializer import CellSerializer


class BoardSerializer(serializers.ModelSerializer):
    cells = serializers.SerializerMethodField()

    def get_cells(self, obj=None):
        cells = []
        for c in Cell.objects.filter(board=obj):
            cells.append(CellSerializer(c).data)
        return cells

    class Meta:
        model = Board
        fields = [   
                    'owner', 
                    'agressor',
                    'uuid',
                    'cells'
                    ]


