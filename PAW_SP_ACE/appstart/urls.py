from django.urls import path
from . import views

urlpatterns = [
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
]