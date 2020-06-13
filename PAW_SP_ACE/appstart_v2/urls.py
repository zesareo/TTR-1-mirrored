from django.urls import path, re_path
from . import views
from rest_framework.authtoken.views import obtain_auth_token  # <-- Here

urlpatterns = [
    
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  # <-- And here POST METHOD
    re_path(r'^Usuario/$', views.UsuarioList.as_view() ),
    re_path(r'^Usuario/(?P<pk>[0-9]+)$', views.UsuarioDetails.as_view() ),    
]