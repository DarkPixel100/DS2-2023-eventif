from django.db import models


class Contact(models.Model):
    name = models.CharField("nome", max_length=255)
    email = models.EmailField("email")
    phone = models.CharField("telefone", max_length=15, blank=True)
    message = models.TextField("mensagem", max_length=1023)
    created_at = models.DateTimeField("realizado em", auto_now_add=True)
    response = models.TextField("resposta", blank=True)
    updated_at = models.DateTimeField("atualizado em", auto_now_add=True)
    replied = models.BooleanField("respondido", default=False)

    class Meta:
        verbose_name = "contato"
        verbose_name_plural = "contatos"
        ordering = ["-created_at", "replied"]

    def __str__(self):
        return self.name
