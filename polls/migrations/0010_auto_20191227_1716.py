# Generated by Django 3.0.1 on 2019-12-27 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_auto_20191227_1542'),
    ]

    operations = [
        migrations.RenameField(
            model_name='investment',
            old_name='date',
            new_name='invest date',
        ),
        migrations.AlterField(
            model_name='entry',
            name='entry_date_date',
            field=models.DateField(verbose_name='entry date'),
        ),
    ]
