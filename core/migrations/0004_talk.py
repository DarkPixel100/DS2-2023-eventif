# Generated by Django 4.2.1 on 2023-12-04 13:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0003_contactspeaker"),
    ]

    operations = [
        migrations.CreateModel(
            name="Talk",
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
                ("title", models.CharField(max_length=200, verbose_name="título")),
                (
                    "start",
                    models.TimeField(blank=True, null=True, verbose_name="início"),
                ),
                ("description", models.TextField(blank=True, verbose_name="descrição")),
                (
                    "speakers",
                    models.ManyToManyField(
                        blank=True, to="core.speaker", verbose_name="palestrantes"
                    ),
                ),
            ],
            options={
                "verbose_name": "palestra",
                "verbose_name_plural": "palestras",
            },
        ),
    ]
