from django.contrib import admin
from django.utils import timezone
from contact.models import Contact


class ContactModelAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "email",
        "phone",
        "created_at",
        "updated_at",
        "replied",
    )
    date_hierarchy = "created_at"
    search_fields = [
        "name",
        "email",
        "phone",
        "message",
        "created_at",
        "updated_at",
        "response",
    ]
    list_filter = ["created_at", "updated_at", "replied"]

    actions = ["mark_as_replied"]

    def mark_as_replied(self, request, queryset):
        count = queryset.update(replied=True)

        if count == 1:
            msg = "{} mensagem foi respondida."
        else:
            msg = "{} mensagens foram respondidas."

        self.message_user(request, msg.format(count))

    mark_as_replied.short_description = "Marcar como \"Respondido\""

    def save_model(self, request, obj, form, change):
        if not obj.replied and "response" in form.changed_data and obj.response.strip():
            obj.replied = True
            form.changed_data.append("replied")

        if "updated_at" not in form.changed_data:
            obj.updated_at = timezone.now()
            form.changed_data.append("updated_at")

        obj.save(update_fields=form.changed_data)


admin.site.register(Contact, ContactModelAdmin)
