# Generated by Django 2.1.2 on 2018-10-08 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jogo', '0003_partida_last_card'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carta',
            name='cor',
            field=models.IntegerField(blank=True, choices=[(0, 'Vermelho'), (1, 'Amarelo'), (2, 'Verde'), (3, 'Azul')], null=True, verbose_name='cor da carta'),
        ),
        migrations.AlterField(
            model_name='carta',
            name='numero',
            field=models.IntegerField(blank=True, null=True, verbose_name='número da carta'),
        ),
    ]
