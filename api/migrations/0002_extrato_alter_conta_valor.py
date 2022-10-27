# Generated by Django 4.1.2 on 2022-10-27 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Extrato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado')),
                ('update_at', models.DateTimeField(auto_now_add=True, verbose_name='Atualizado')),
                ('disponivel', models.BooleanField(default=True, verbose_name='Status')),
                ('conta', models.CharField(max_length=225, verbose_name='conta')),
                ('valor', models.FloatField(verbose_name='Valor')),
                ('descricao', models.TextField(blank=True, verbose_name='Descrição')),
            ],
            options={
                'verbose_name': 'Extrato',
            },
        ),
        migrations.AlterField(
            model_name='conta',
            name='valor',
            field=models.FloatField(verbose_name='Valor'),
        ),
    ]