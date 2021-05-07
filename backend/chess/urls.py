from chess.views.create_board import CreateBoardView
from django.urls import path, include
from chess.views import GoogleView, GetBoardView, CreateBoardView, AddAgressorBoardView, GetFiguresView, EmailAuthView, SetFigureView, MoveFigureView, GamesView, LoadClassicBoardView

 

urlpatterns = [ 
        path('login/', GoogleView.as_view()),
        path('get/board', GetBoardView.as_view()),
        path('games', GamesView.as_view()),
        path('get/figures', GetFiguresView.as_view()),
        path('load/classic/board/<str:board_id>', LoadClassicBoardView.as_view()),
        path('set/figure', SetFigureView.as_view()),
        path('move/figure', MoveFigureView.as_view()),
        path('login/byemail', EmailAuthView.as_view()),
        path('get/board/<str:board_id>', GetBoardView.as_view()),
        path('create/board', CreateBoardView.as_view()),
        path('add/agressor/<str:board_id>', AddAgressorBoardView.as_view()),
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