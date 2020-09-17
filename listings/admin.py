from django.contrib import admin

from .models import Listing

class ListAdmin(admin.ModelAdmin):
    list_display=('id','title','is_published','price' )
    list_display_links=('id', 'title', 'price')
    list_editable=('is_published',)
    list_filter=('price','state')
    search_fields=('id','title','is_published','price','state', 'city','zipcode','garage')
    list_per_page=20
admin.site.register(Listing, ListAdmin)
