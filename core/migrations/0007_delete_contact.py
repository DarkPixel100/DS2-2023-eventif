# Generated by Django 4.2.1 on 2023-12-04 14:07

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0006_alter_contact_message_alter_contact_phone"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Contact",
        ),
    ]
