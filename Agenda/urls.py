from django.urls import path, include
from rest_framework.routers import DefaultRouter

from Agenda.models import Contato, Telefone, Email, Emergencia
from Agenda.views import ContatoViewSet, TelefoneViewSet, EmailViewSet, EmergenciaViewSet

router = DefaultRouter()

router.register(r'contato', ContatoViewSet)

router.register(r'telefone', TelefoneViewSet)

router.register(r'email', EmailViewSet)

router.register(r'emergencia', EmergenciaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]