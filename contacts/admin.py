from django.contrib import admin

from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display=('listing_id', 'listing', 'name', 'email' )
    list_display_links=('listing_id', 'name')
    search_fields=('listing_id','listing','name','email')
    list_per_page=20
admin.site.register(Contact, ContactAdmin)
