from django.urls import path, include
from rest_framework.routers import DefaultRouter

from Agenda.models import Contato, Telefone, Email
from Agenda.views import ContatoViewSet, TelefoneViewSet, EmailViewSet

router = DefaultRouter()

router.register(r'contato', ContatoViewSet)

router.register(r'telefone', TelefoneViewSet)

router.register(r'email', EmailViewSet)

# router.register(r'emergencia', EmergenciaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]