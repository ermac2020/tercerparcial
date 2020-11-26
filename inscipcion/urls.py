
from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url('inscripcion/nuevo/', views.inscripcion_nuevo, name='inscripcion_nuevo'),
    path('inscripcion/lista/', views.inscripcion_lista, name='inscripcion_lista'),
    path('inscripcion/<int:pk>/', views.inscripcion_detalle, name='inscripcion_detalle'),
    url('', views.principal, name='principal'),
]
