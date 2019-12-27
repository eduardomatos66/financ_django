from decimal import Decimal

from django.core.validators import MinValueValidator
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
    entry_date_date = models.DateField('entry_date')
    entry_type_text = models.CharField(name='type', max_length=30, choices=EntryType.choices,
                                       default=EntryType.OUT_CHOICE)
    entry_area_text = models.CharField(name='area', max_length=30, choices=EntryAreaType.choices,
                                       default=EntryAreaType.N_A)
    entry_with_text = models.CharField(name='entry_with', max_length=200, default="")
    entry_origin_dest_text = models.CharField(name='origin_dest', max_length=200)
    entry_payment_type = models.CharField(name='payment_type', max_length=200, default="")
    entry_value = models.DecimalField(name='value', decimal_places=2, max_digits=12, default=0.00,
                                      validators=[MinValueValidator(Decimal('0.01'))])
    entry_realized_bool = models.BooleanField(name='realized', default=False)

    def __str__(self):
        return "date: {date}\n type: {type}\n area: {area}\n with: {_with}\n origin_dest: {origin_dest}\n " \
               "payment: {payment}\n value: {value}\n done: {done}\n ".format(
                                                    date=self.entry_date_date,
                                                    type=self.type,
                                                    area=self.area,
                                                    _with=self.entry_with,
                                                    origin_dest=self.origin_dest,
                                                    payment=self.payment_type,
                                                    value=self.value,
                                                    done=self.realized)


class Investment(models.Model):
    date_date = models.DateField(name='invest_date')
    duedate_date = models.DateField(name='due_date')
    paper_name_text = models.CharField(name='paper_name', max_length=200, default="")
    number_paper_text = models.DecimalField(name='number_paper', decimal_places=2, max_digits=12, default=0.00,
                                            validators=[MinValueValidator(Decimal('0.01'))])
    price_paper_text = models.DecimalField(name='paper_price', decimal_places=2, max_digits=12, default=0.00,
                                           validators=[MinValueValidator(Decimal('0.01'))])
    type_text = models.CharField(name='type', max_length=200, default="")
    where_text = models.CharField(name='where', max_length=200, default="")
    investment_value = models.DecimalField(name='value', decimal_places=2, max_digits=12, default=0.00,
                                           validators=[MinValueValidator(Decimal('0.01'))])

    def __str__(self):
        return "date: {date}\n duedate: {duedate}\n paper: {paper}\n number: {number}\n paper_price: {paper_price}\n" \
               " type: {type}\n where: {where}\n investment: {investment}\n ".format(
                                                                        date=self.invest_date,
                                                                        duedate=self.due_date,
                                                                        paper=self.paper_name,
                                                                        number=self.number_paper,
                                                                        paper_price=self.paper_price,
                                                                        type=self.type,
                                                                        where=self.where,
                                                                        investment=self.value)
