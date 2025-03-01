# Generated by Django 4.2.1 on 2023-11-03 11:40

from django.db import migrations, models
import subscriptions.validators


class Migration(migrations.Migration):

    dependencies = [
        ("subscriptions", "0002_alter_subscription_options_subscription_paid_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="subscription",
            name="cpf",
            field=models.CharField(
                max_length=11,
                validators=[subscriptions.validators.validate_cpf],
                verbose_name="CPF",
            ),
        ),
        migrations.AlterField(
            model_name="subscription",
            name="email",
            field=models.EmailField(blank=True, max_length=254, verbose_name="e-mail"),
        ),
        migrations.AlterField(
            model_name="subscription",
            name="paid",
            field=models.BooleanField(default=False, verbose_name="pago"),
        ),
        migrations.AlterField(
            model_name="subscription",
            name="phone",
            field=models.CharField(blank=True, max_length=20, verbose_name="telefone"),
        ),
    ]
