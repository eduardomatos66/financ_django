# Generated by Django 3.0.1 on 2019-12-27 15:26

from decimal import Decimal
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_auto_20191227_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='value',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=12, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))]),
        ),
    ]
