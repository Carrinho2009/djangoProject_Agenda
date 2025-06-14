from rest_framework import viewsets
from Agenda.models import Contato, Telefone, Email
from Agenda.serializers import ContatoSerializers, TelefoneSerializers, EmailSerializers
from Agenda.filters import ContatoFilter, TelefoneFilter, EmailFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions

class ContatoViewSet(viewsets.ModelViewSet):
    queryset = Contato.objects.all()
    serializer_class = ContatoSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_class = ContatoFilter
    # permission_classes = [permissions.IsAuthenticated]

class TelefoneViewSet(viewsets.ModelViewSet):
    queryset = Telefone.objects.all()
    serializer_class = TelefoneSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_class = TelefoneFilter
    # permission_classes = [permissions.IsAuthenticated]

class EmailViewSet(viewsets.ModelViewSet):
    queryset = Email.objects.all()
    serializer_class = EmailSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_class = EmailFilter
    # permission_classes = [permissions.IsAuthenticated]

# class EmergenciaViewSet(viewsets.ModelViewSet):
#     queryset = Emergencia.objects.all()
#     serializer_class = EmergenciaSerializers
#     filter_backends = [DjangoFilterBackend]
#     filterset_class = EmergenciaFilter
#     # permission_classes = [permissions.IsAuthenticated]