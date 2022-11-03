from django.contrib import admin

from .models import Painting, MainPainting, Photo


class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 1
    

class PaintingAdmin(admin.ModelAdmin):
    inlines = [PhotoInline,]
    list_display = ['title', 'date']
    
    
admin.site.register(MainPainting)
admin.site.register(Painting, PaintingAdmin)