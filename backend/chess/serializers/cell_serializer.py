
from rest_framework import serializers
from chess.models import Cell
from .figure_serializer import FigureSerializer



class CellSerializer(serializers.ModelSerializer):
    figure = FigureSerializer()
    
    class Meta:
        model = Cell
        fields = [    
                    'figure',
                    'color',
                    'id'
                    ]

