# Generated by Django 5.1.1 on 2024-10-08 23:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("receitas", "0005_alter_receita_pessoa"),
    ]

    operations = [
        migrations.AddField(
            model_name="receita",
            name="publicada",
            field=models.BooleanField(default=False),
        ),
    ]
