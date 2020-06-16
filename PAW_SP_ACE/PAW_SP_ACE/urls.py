"""PAW_SP_ACE URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework_simplejwt import views as jwt_views

'''
    Documentacion Rest Framework 
'''
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

'''
    Adding login to the Browsable API https://www.django-rest-framework.org/tutorial/4-authentication-and-permissions/
'''
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/appstart/', include('appstart.urls')),
    path('core/', include('core.urls')),
    path('token/obtain/', jwt_views.TokenObtainPairView.as_view(), name='token_create'),  # override sjwt stock token
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api/appstart/v2/', include('appstart_v2.urls')),
    path('admin/doc/', include('django.contrib.admindocs.urls')), #Documentacion Django
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'), #Documentacion DRF
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'), #Documentacion DRF
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'), #Documentacion DRF  
    ##login browsable API, no incluir si no se requiere autenticacion de la API
    path('api-auth/', include('rest_framework.urls')), 
]
