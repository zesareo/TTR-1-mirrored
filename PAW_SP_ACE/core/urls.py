from django.urls import path
from .views import current_user, UserList
from rest_framework.authtoken.views import obtain_auth_token  # <-- Here
#from rest_framework_jwt import views as jwt_views

from rest_framework.authtoken.views import obtain_auth_token  # <-- Here
urlpatterns = [
    path('current_user/', current_user),
    path('users/', UserList.as_view()),
    path('token-auth/', obtain_auth_token,),  # <-- And here POST METHOD
    #path('token-auth/', obtain_jwt_token)
]