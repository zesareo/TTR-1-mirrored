from django.urls import path, re_path, include
from . import views

urlpatterns = [
    #Refencia a vistas basadas en clases && Vistas con clases genericas y mixins

    #path('Usuario', views.UsuarioListCreate.as_view() ),
    path('Alumno', views.AlumnoListCreate.as_view() ),
    path('Agente', views.AgenteListCreate.as_view() ),
    path('Materia', views.MateriaListCreate.as_view() ),
    path('ETS', views.ETSListCreate.as_view() ),
    #path('Alumno_ETS', views.Alumno_ETSListCreate.as_view() ),
    path('Tipo_Tramite', views.Tipo_tramiteListCreate.as_view() ), #Use Capital letters in Tramite because browser converter to Capital in automatic
    path('Tramite', views.TramiteListCreate.as_view() ),
    path('Tipo_Archivo', views.Tipo_archivoListCreate.as_view() ), #Use Capital letters in Archivo because browser converter to Capital in automatic
    path('Archivo_Adjunto', views.Archivo_adjuntoListCreate.as_view() ), #Use Capital letters in Adjunto because browser converter to Capital in automatic
    re_path(r'^appstartv2/Usuario/$', views.UsuarioList.as_view() ),
    re_path(r'^appstartv2/Usuario/(?P<pk>[0-9]+)$', views.UsuarioDetails.as_view() ),
   
    re_path(r'^appstartv2/Tramite/$', views.UsuarioList.as_view() ),
    re_path(r'^appstartv2/Tramite/(?P<pk>[0-9]+)$', views.UsuarioDetails.as_view() ),
    
    #Refencia a vistas basadas en funciones
    
    #re_path(r'^func/Usuario/$', views.usuario_list),
    re_path('func/Usuario', views.usuario_list),
    re_path('func/Usuario/', views.usuario_list),
    re_path('func/Usuario/(?P<pk>[0-9]+)$', views.usuario_details),
]
