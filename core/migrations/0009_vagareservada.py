# Generated by Django 3.2.6 on 2021-08-06 23:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_movmensalista'),
    ]

    operations = [
        migrations.CreateModel(
            name='VagaReservada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.mensalista')),
                ('veiculo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.veiculo')),
            ],
        ),
    ]
