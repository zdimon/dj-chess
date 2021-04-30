
from rest_framework import serializers
from chess.models import Cell



class CellSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = Cell
        fields = [   
                    'board', 
                    'figure',
                    'color',
                    'id'
                    ]

