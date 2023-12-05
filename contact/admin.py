from django.contrib import admin
from contact.models import Contact


class ContactModelAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "email",
        "phone",
        "message",
        "created_at",
    )
    date_hierarchy = "created_at"
    search_fields = ["name", "email", "phone", "message", "created_at"]
    list_filter = [
        "created_at",
    ]


admin.site.register(Contact, ContactModelAdmin)