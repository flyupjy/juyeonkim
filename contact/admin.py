from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    model = Contact
    list_display = ['sender', 'subject', 'sent_at']
    ordering = ('-sent_at',)

admin.site.register(Contact, ContactAdmin)