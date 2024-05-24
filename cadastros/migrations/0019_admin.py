# Generated by Django 5.0.6 on 2024-05-18 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cadastros", "0018_delete_admin"),
    ]

    operations = [
        migrations.CreateModel(
            name="Admin",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "nome",
                    models.CharField(
                        help_text="Digite o nome aqui.",
                        max_length=100,
                        verbose_name="Nome",
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        error_messages={
                            "blank": "Este campo não pode ficar em branco.",
                            "invalid": "O valor fornecido é inválido, verifique se tem @.",
                        },
                        help_text="Digite o E-mail aqui.",
                        max_length=255,
                        unique=True,
                        verbose_name="E-mail",
                    ),
                ),
                ("senha", models.CharField(max_length=100)),
                (
                    "telefone",
                    models.CharField(
                        blank=True,
                        help_text="Digite seu Telefone aqui. (21) 90000-0000",
                        max_length=15,
                        verbose_name="Telefone",
                    ),
                ),
                (
                    "cpf",
                    models.CharField(
                        blank=True,
                        help_text="Digite seu CPF aqui modelo: 000.000.000-00",
                        max_length=14,
                        unique=True,
                        verbose_name="CPF",
                    ),
                ),
            ],
        ),
    ]