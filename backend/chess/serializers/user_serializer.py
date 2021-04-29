from rest_framework import serializers
from chess.models import UserProfile



class UserSerializer(serializers.HyperlinkedModelSerializer):
    

    class Meta:
        model = UserProfile
        fields = [  'id', 
                    'publicname', 
                    'username'
                    ]

