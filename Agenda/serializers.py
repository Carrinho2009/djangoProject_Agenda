from rest_framework import serializers

from Agenda.models import Contato, Email, Telefone, Emergencia

class ContatoSerializers(serializers.ModelSerializer):
    name = serializers.CharField(max_length=70)
    age = serializers.IntegerField(min_value=12, max_value=100)

    class Meta:
        model = Contato
        fields = '__all__'

class EmailSerializers(serializers.ModelSerializer):
    dominio = serializers.CharField(min_length=11,max_length=30)
    email = serializers.CharField(max_length=30)

    class Meta:
        model = Email
        fields = '__all__'

class TelefoneSerializers(serializers.ModelSerializer):
    codigo_telefone = serializers.CharField(min_length=2,max_length=2)
    Numerotelefone = serializers.CharField(min_length=11,max_length=11)

    class Meta:
        model = Telefone
        fields = '__all__'

class EmergenciaSerializers(serializers.ModelSerializer):
    Parentesco = serializers.CharField(min_length=2,max_length=2)

    class Meta:
        model = Emergencia
        fields = '__all__'