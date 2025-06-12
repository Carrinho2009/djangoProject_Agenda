from django.db import models

# Create your models here.
class ModelBase(models.Model):
    id = models.BigAutoField(
        db_column='id',
        null=False,
        primary_key=True
    )
    created_at = models.DateTimeField(
        db_column='dt_created',
        auto_now_add=True,
        null=True
    )
    modified_at = models.DateTimeField(
        db_column='dt_modified',
        auto_now=True,
        null=True
    )
    active = models.BooleanField(
        db_column='cs_active',
        null=False,
        default=True
    )

    class Meta:
        abstract = True
        managed = True


class Contato(ModelBase):
    name = models.CharField(
        db_column='tx_contato',
        max_length=70,
        null=False
    )
    age = models.IntegerField(
        db_column='nb_idade',
        null=False
    )

def __str__(self):
    return f'{self.name} - {self.age}'


class Email(ModelBase):
    contato = models.ForeignKey(
        Contato,
        db_column='tx_contato',
        null=False,
        on_delete=models.CASCADE
    )
    dominio = models.CharField(
        db_column='tx_dominio',
        max_length=70,
        null=False
    )
    email = models.EmailField(
        db_column='tx_email',
        null=False
    )


    def __str__ (self):
        return f'{self.dominio} - {self.email}'

class Telefone(ModelBase):
   Contato = models.ForeignKey(
       Contato,
       db_column='tx_contato',
       null=False,
       on_delete=models.CASCADE
   )
   email = models.ForeignKey(
       Email,
       db_column='tx_email',
       null=False,
       on_delete=models.CASCADE
   )
   codigo_telefone = models.CharField(
       db_column='tx_codigo_telefone',
       max_length=2,
       null=False
   )
   NumeroTelefone = models.IntegerField(
       db_column='tx_numero_telefone',
       max_length=11,
       null=False
   )

   def __str__(self):
        return f'{self.id} - {self.codigo_telefone} - {self.NumeroTelefone}'

class Emergencia(ModelBase):
    Contato = models.ForeignKey(
        Contato,
        db_column='tx_contato',
        null=False,
        on_delete=models.CASCADE
    )
    Email = models.ForeignKey(
        Email,
        db_column='tx_email',
        null=False,
        on_delete=models.CASCADE
    )
    Telefone = models.ForeignKey(
        Telefone,
        db_column='tx_telefone',
        null=False,
        on_delete=models.CASCADE
    )
    Parentesco = models.IntegerField(
        db_column='tx_parentesco',
        max_length=16,
        null=False,
    )

    def __str__(self):
        return f'{self.id} - {self.Email} - {self.Telefone} - {self.Parentesco}'

#Contato, on_delete=models.CASCADE
