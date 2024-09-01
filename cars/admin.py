from django.contrib import admin
from .models import Car
from django.utils.html import format_html

# Inregistreaza modelele auto aici
class CarAdmin(admin.ModelAdmin):

    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;" />' .format(object.poza.url))
    
    thumbnail.short_description= 'poza'

    list_display = ( 'serie_Sasiu','thumbnail', 'car_title', 'judet', 'culoare', 'model','an','caroserie','tip_combustibil','is_featured')
    list_display_links = ( 'serie_Sasiu','thumbnail','car_title')
    list_editable = ('is_featured',)
    search_fields = ('id', 'car_title', 'judet', 'model', 'caroserie', 'tip_combustibil')
    list_filter = ('judet', 'model', 'caroserie', 'tip_combustibil')


admin.site.register(Car, CarAdmin)
