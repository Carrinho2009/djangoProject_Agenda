import django_filters

from Agenda.models import Contato, Email, Telefone


class ContatoFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    age = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Contato
        fields = ['name', 'age']

class EmailFilter(django_filters.FilterSet):
    dominio = django_filters.CharFilter(lookup_expr='exact')
    email = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Email
        fields = ['dominio', 'email']

class TelefoneFilter(django_filters.FilterSet):
    codigo_telefone= django_filters.CharFilter(lookup_expr='exact')
    NumeroTelefone = django_filters.CharFilter(lookup_expr='exact')

    class Meta:
        model = Telefone
        fields = ['codigo_telefone', 'NumeroTelefone']

# class EmergenciaFilter(django_filters.FilterSet):
#     Parentesco = django_filters.CharFilter(lookup_expr='exact')
#
#     class Meta:
#         model = Emergencia
#         fields = ['Parentesco']