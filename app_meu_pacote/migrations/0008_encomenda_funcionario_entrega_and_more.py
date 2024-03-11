# Generated by Django 4.1.7 on 2023-05-12 03:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_meu_pacote', '0007_funcionario_condominio'),
    ]

    operations = [
        migrations.AddField(
            model_name='encomenda',
            name='funcionario_entrega',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='funcionario_entrega', to='app_meu_pacote.funcionario'),
        ),
        migrations.AddField(
            model_name='encomenda',
            name='funcionario_recebimento',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='funcionario_recebimento', to='app_meu_pacote.funcionario'),
            preserve_default=False,
        ),
    ]