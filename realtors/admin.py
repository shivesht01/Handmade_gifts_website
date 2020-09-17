from django.contrib import admin

from .models import Realtor
class Listadmin(admin.ModelAdmin):
    list_display=('name','photo','email')
    list_display_links=('name',)

admin.site.register(Realtor,Listadmin)
