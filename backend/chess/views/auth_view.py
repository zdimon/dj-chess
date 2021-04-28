
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from drf_yasg.utils import swagger_auto_schema

from chess.serializers import GoogleAuthRequestSerializer, UserSerializer

from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from chess.models import UserProfile, SocialAuth

class GoogleView(APIView):
    '''
    Google authorization.

    _______________________

    '''
    
    permission_classes = ()
    authentication_classes = ()
    @swagger_auto_schema( 
        request_body = GoogleAuthRequestSerializer \
        )
    def post(self, request, format=None):
        try:
            u = User.objects.get(username=request.data['email'])
            token, created = Token.objects.get_or_create(user=u)
            user = u.userprofile
        except Exception as e:
            print(str(e))
            user = UserProfile()
            user.username = request.data['email']
            user.publicname = request.data['name']
            user.is_active = True
            user.set_password = '123'
            user.save()
            token = Token.objects.create(user=user)
            s = SocialAuth()
            s.type = 'GOOGLE'
            s.email = request.data['email']
            s.user = user
            s.save()

        return Response({
            'token': token.key,
            'agent': request.META['HTTP_USER_AGENT'],
            'user': UserSerializer(user).data
        })