from django.db import models


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


class Hospede(ModelBase):
    nome = models.CharField(
        db_column='tx_nome',
        max_length=255,
        null=False,

    )
    cpf = models.CharField(
        db_column='tx_cpf',
        max_length=14,
        unique=True
    )
    telefone = models.CharField(
        max_length=20,
        null=True
    )

    idade = models.IntegerField(
        db_column='tx_idade',
        null=True
    )
    genero = models.CharField(
        max_length=50,
        null=True
    )

    def __str__(self):
        return self.nome


class Quarto(ModelBase):
    CASAL = 'casal'
    SOLTEIRO = 'solteiro'
    TIPOS_CHOICES = [
        ('CASAL', 'Casal'),
        ('SOLTEIRO', 'Solteiro'),
    ]

    tipo = models.CharField(
        max_length=20,
        choices=TIPOS_CHOICES, default='SOLTEIRO'
    )

    valor_diaria = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    def __str__(self):
        return f"Quarto {self.tipo} - R$ {self.valor_diaria}"


class Reserva(ModelBase):
    hospede = models.ForeignKey(
        Hospede,
        db_column='tx_hospede',
        null=False,
        on_delete=models.DO_NOTHING
    )

    quarto = models.ForeignKey(
        Quarto,
        db_column='tx_quarto',
        null=False,
        on_delete=models.DO_NOTHING
    )

    valor_total = models.DecimalField(
        max_digits=10,
        decimal_places=2

    )
    data_entrada = models.DateField(
        auto_now_add=True,
    )
    data_saida = models.DateField()
    quantidade_dias = models.IntegerField()

    def __str__(self):

        return f"Reserva de {self.hospede.nome} no quarto {self.quarto.tipo}"
