from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.authentication import TokenAuthentication, SessionAuthentication


schema_view = get_schema_view(
   openapi.Info(
      title="Maga API",
      default_version='v1',
      description="MAGA API Reference",
      terms_of_service="https://who-was-maga-antoine.info/",
      contact=openapi.Contact(url='https://who-was-maga-antoine.info'),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
   authentication_classes=(TokenAuthentication,)
)

urlpatterns = [
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='docs-ui'),
    
    path('v1/', include(('core.urls', 'core'))),
]
