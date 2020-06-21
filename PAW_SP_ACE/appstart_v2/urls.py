from django.urls import path, re_path
from . import views
from rest_framework.authtoken.views import obtain_auth_token  # <-- Here

urlpatterns = [
    
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  # <-- And here POST METHOD
    re_path(r'^Usuario/$', views.UsuarioList.as_view() ),  #OKKKK
    re_path(r'^Usuario/(?P<pk>[0-9]+)$', views.UsuarioDetails.as_view() ),    
    
    re_path(r'^Alumno/$', views.AlumnoList.as_view() ),  
    re_path(r'^Alumno/(?P<pk>[0-9]+)$', views.AlumnoDetails.as_view() ),    
    
    re_path(r'^Agente/$', views.AgenteList.as_view() ),  
    re_path(r'^Agente/(?P<pk>[0-9]+)$', views.AgenteDetails.as_view() ),   
      
    re_path(r'^Materia/$', views.MateriaList.as_view() ),  
    re_path(r'^Materia/(?P<pk>[0-9]+)$', views.MateriaDetails.as_view() ),   

    re_path(r'^ETS/$', views.ETSList.as_view() ),  
    re_path(r'^ETS/(?P<pk>[0-9]+)$', views.ETSDetails.as_view() ),    

    re_path(r'^Tipo_Tramite/$', views.Tipo_tramiteList.as_view() ),  
    re_path(r'^Tipo_Tramite/(?P<pk>[0-9]+)$', views.Tipo_tramiteDetails.as_view() ),      

    re_path(r'^Tramite/$', views.TramiteList.as_view() ),  
    re_path(r'^Tramite/(?P<pk>[0-9]+)$', views.TramiteDetails.as_view() ),   

    re_path(r'^Tipo_Archivo/$', views.Tipo_archivoList.as_view() ),  
    re_path(r'^Tipo_Archivo/(?P<pk>[0-9]+)$', views.Tipo_archivoDetails.as_view() ),     
      
    re_path(r'^Archivo_Adjunto/$', views.Archivo_adjuntoList.as_view() ),  
    re_path(r'^Archivo_Adjunto/(?P<pk>[0-9]+)$', views.Archivo_adjuntoDetails.as_view() ),    
   
    re_path(r'^Alumno_ETS/$', views.Alumno_ETSList.as_view() ),  
    re_path(r'^Alumno_ETS/(?P<pk>[0-9]+)$', views.Alumno_ETSDetails.as_view() ),

    re_path(r'^Alumno_ETS/by/(?P<alumno>[0-9]+)$', views.Alumno_ETSBY.as_view() ),  
    re_path(r'^Alumno_ETSDescripcion/by/(?P<alumno>[0-9]+)$', views.Alumno_ETSDescripcionBY.as_view() ), 

    re_path(r'^Alumno_ETSDescripcion/', views.Alumno_ETSDescripcion.as_view() ),
    #?P<make>\w+)/$'

    re_path(r'^Tramite/by/(?P<alumno>[0-9]+)$', views.TramiteBY.as_view() ),
    re_path(r'^TramiteFase1/$', views.TramiteFase1List.as_view() ),
    #re_path(r'^Documento_Firmado/(?P<LlavePublica>\w+)$', views.Documento_FirmadoList.as_view() ), 
    
   
   
]