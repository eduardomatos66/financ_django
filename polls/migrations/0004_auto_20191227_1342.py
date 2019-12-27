# Generated by Django 3.0.1 on 2019-12-27 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20191227_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='entry_area_text',
            field=models.CharField(choices=[('alimentacao', 'ALIMENTACAO'), ('bancos', 'BANCOS'), ('calcados', 'CALCADOS'), ('cama_mesa_banho', 'CAMA/MESA/BANHO'), ('diversao', 'DIVERSAO'), ('eletronico', 'ELETRONICO'), ('estudo', 'ESTUDO'), ('higiene', 'HIGIENE'), ('investimento', 'INVESTIMENTO'), ('moradia', 'MORADIA'), ('moveis', 'MOVEIS'), ('roupas', 'ROUPAS'), ('saude', 'SAUDE'), ('telefonia', 'TELEFONIA'), ('transporte', 'TRANSPORTE'), ('n_a', 'N/A')], default='n_a', max_length=30),
        ),
        migrations.AlterField(
            model_name='entry',
            name='entry_type_text',
            field=models.CharField(choices=[('in', 'IN'), ('out', 'OUT')], default='out', max_length=30),
        ),
    ]
