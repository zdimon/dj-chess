from django.contrib import admin
from django.urls import path, include
from chess.views import index

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

from rest_framework import routers
router = routers.DefaultRouter()

schema_view = get_schema_view(
   openapi.Info(
      title="Chess game API",
      default_version='v1',
      description=''' 
          Documentation `ReDoc` view can be found [here](/doc).

          Admin interfase  [here](/admin).

          Authors: zdimon77@gmail.com
      ''',
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)



urlpatterns = [
    path('', index),
    path('chess', index),
    path('login', index),
    path('admin/', admin.site.urls),
    path('api', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('v1/',include([
        path('chess/',include('chess.urls')),
        path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    ])),

]


from django.conf import settings
from django.conf.urls.static import static

urlpatterns = urlpatterns + static(settings.MEDIA_URL, 
                                   document_root=settings.MEDIA_ROOT)