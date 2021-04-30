
from rest_framework import serializers
from chess.models import User2Figure, Figure

class FigureDetailSerializer(serializers.ModelSerializer):


    class Meta:
        model = Figure
        fields = [   
                    'name', 
                    'get_image_absolute_url',
                    'color'
                    ]

class FigureSerializer(serializers.ModelSerializer):
    figure = FigureDetailSerializer()
    
    class Meta:
        model = User2Figure
        fields = [   
                    'board', 
                    'figure',
                    'user',
                    'id'
                    ]


class FiguresSerializer(serializers.Serializer):
    figures = serializers.SerializerMethodField()
    def get_figures(self, obj=None):
        figures = []
        print('sssssssssssss')
        for c in User2Figure.objects.all():
            figures.append(FigureSerializer(c).data)
            print(c)
        return figures