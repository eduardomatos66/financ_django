from django.db import models
from django.utils.translation import gettext_lazy as _


class EntryType(models.TextChoices):
    IN_CHOICE = "in", _("IN")
    OUT_CHOICE = "out", _("OUT")


class EntryAreaType(models.TextChoices):
    ALIMENTACAO = "alimentacao", _("ALIMENTACAO")
    BANCOS = "bancos", _("BANCOS")
    CALCADOS = "calcados", _("CALCADOS")
    CAMA_MESA_BANHO = "cama_mesa_banho", _("CAMA/MESA/BANHO")
    DIVERSAO = "diversao", _("DIVERSAO")
    ELETRONICO = "eletronico", _("ELETRONICO")
    ESTUDO = "estudo", _("ESTUDO")
    HIGIENE = "higiene", _("HIGIENE")
    INVESTIMENTO = "investimento", _("INVESTIMENTO")
    MORADIA = "moradia", _("MORADIA")
    MOVEIS = "moveis", _("MOVEIS")
    ROUPAS = "roupas", _("ROUPAS")
    SAUDE = "saude", _("SAUDE")
    TELEFONIA = "telefonia", _("TELEFONIA")
    TRANSPORTE = "transporte", _("TRANSPORTE")
    N_A = "n_a", _("N/A")


class Entry(models.Model):
    entry_date_date = models.DateField('date')
    entry_type_text = models.CharField(name='type', max_length=30, choices=EntryType.choices, default=EntryType.OUT_CHOICE)
    entry_area_text = models.CharField(name='area', max_length=30, choices=EntryAreaType.choices, default=EntryAreaType.N_A)
    entry_with_text = models.CharField(name='with', max_length=200, default="")
    entry_origin_dest_text = models.CharField(name='origin/dest', max_length=200)
    entry_payment_type = models.CharField(name='payment', max_length=200, default="")
    entry_value = models.DecimalField(name='value', decimal_places=2, max_digits=12, default=0.00)
    entry_realized_bool = models.BooleanField(name='realized', default=False)


class Investment(models.Model):
    date_date = models.DateField('date')
    duedate_date = models.DateField('date')
    paper_name_text = models.CharField(max_length=200, default="")
    type_text = models.CharField(max_length=200, default="")
    where_text = models.CharField(max_length=200, default="")
    investment_value = models.DecimalField(decimal_places=2, max_digits=12, default=0.00)
