from django.urls import path, re_path, include
from . import views
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    #Refencia a vistas basadas en clases && Vistas con clases genericas y mixins
    path('api/appstart/Usuario', views.UsuarioListCreate.as_view() ),
    path('api/appstart/Alumno', views.AlumnoListCreate.as_view() ),
    path('api/appstart/Agente', views.AgenteListCreate.as_view() ),
    path('api/appstart/Materia', views.MateriaListCreate.as_view() ),
    path('api/appstart/ETS', views.ETSListCreate.as_view() ),
    path('api/appstart/Alumno_ETS', views.Alumno_ETSListCreate.as_view() ),
    path('api/appstart/Tipo_Tramite', views.Tipo_tramiteListCreate.as_view() ), #Use Capital letters in Tramite because browser converter to Capital in automatic
    path('api/appstart/Tramite', views.TramiteListCreate.as_view() ),
    path('api/appstart/Tipo_Archivo', views.Tipo_archivoListCreate.as_view() ), #Use Capital letters in Archivo because browser converter to Capital in automatic
    path('api/appstart/Archivo_Adjunto', views.Archivo_adjuntoListCreate.as_view() ), #Use Capital letters in Adjunto because browser converter to Capital in automatic
    re_path(r'^api/appstartv2/Usuario/$', views.UsuarioList.as_view() ),
    re_path(r'^api/appstartv2/Usuario/(?P<pk>[0-9]+)$', views.UsuarioDetails.as_view() ),
    path('token-auth/', obtain_jwt_token),
    
    
    #Refencia a vistas basadas en funciones
    
    #re_path(r'^api/appstartv2/Usuario/$', views.usuario_list),
    #re_path(r'^api/appstartv2/Usuario/(?P<pk>[0-9]+)$', views.usuario_details),
]
