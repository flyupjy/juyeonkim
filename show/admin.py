from django.contrib import admin
from .models import Exhibition


class ExhibitionAdmin(admin.ModelAdmin):
    model = Exhibition
    list_display = ('title', 'start_date', 'end_date')

admin.site.register(Exhibition, ExhibitionAdmin)