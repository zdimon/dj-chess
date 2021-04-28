from django.urls import path, include
from chess.views import GoogleView, GetBoardView

urlpatterns = [ 
        path('login/', GoogleView.as_view()),
         path('get/board', GetBoardView.as_view()),
]


# from rest_framework.authtoken import views
# from dj_prj.custom_auth_token import CustomAuthToken
# import oauth2_provider.views as oauth2_views

# from taxi.views import RegionsListView, \
#                        GoogleView, \
#                        UserProfileSaveView, \
#                        AddPointView, \
#                        TripAddView, \
#                        PassengerAddToTripView, \
#                        DriverAddToTripView, \
#                        SearchPointView, \
#                        NotificationListView, \
#                        Region2UserCreateView 



# urlpatterns = [ 
#         path('api-token-auth/', CustomAuthToken.as_view()),
#         path('regions_list',RegionsListView.as_view()),
#         path('google_auth',GoogleView.as_view()),
#         path('profile_save',UserProfileSaveView.as_view()),
#         path('point_add',AddPointView.as_view()),
#         path('trip_add',TripAddView.as_view()),
#         path('passenger_add_to_trip',PassengerAddToTripView.as_view()),
#         #path('driver_add_to_trip',DriverAddToTripView.as_view()),
#         path('point_search',SearchPointView.as_view()),
#         path('notification_list',NotificationListView.as_view()),
#         path('region2user_add',Region2UserCreateView.as_view()),
#         path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),


    
# ]