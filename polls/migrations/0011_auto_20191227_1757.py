# Generated by Django 3.0.1 on 2019-12-27 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0010_auto_20191227_1716'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry',
            old_name='origin/Dest',
            new_name='origin_dest',
        ),
        migrations.RenameField(
            model_name='entry',
            old_name='payment type',
            new_name='payment_type',
        ),
        migrations.RenameField(
            model_name='investment',
            old_name='due date',
            new_name='due_date',
        ),
        migrations.RenameField(
            model_name='investment',
            old_name='invest date',
            new_name='invest_date',
        ),
        migrations.RenameField(
            model_name='investment',
            old_name='number of paper',
            new_name='number_paper',
        ),
        migrations.RenameField(
            model_name='investment',
            old_name='paper name',
            new_name='paper_name',
        ),
        migrations.RenameField(
            model_name='investment',
            old_name='price of paper',
            new_name='paper_price',
        ),
        migrations.AlterField(
            model_name='entry',
            name='entry_date_date',
            field=models.DateField(verbose_name='entry_date'),
        ),
    ]
