# Generated by Django 3.2.6 on 2021-08-05 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_veiculo_proprietario'),
    ]

    operations = [
        migrations.AddField(
            model_name='veiculo',
            name='observacoes',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]