from re import search
from django.contrib import admin
from .models import Owner_Panel,Food_Panel
# # Register your models here.
class owner_panel_admin(admin.ModelAdmin):
    #date_hierarchy = 'created'
    search_fields = ['name','gmail','id','number']
    list_display_links = ['name']
    list_display = ('name','id','gmail','number','owner_priority_serial','Facebook_URL','Linkedin_URL','Instagram_URL','created')
    

admin.site.register(Owner_Panel,owner_panel_admin)
admin.site.register(Food_Panel)

admin.site.site_header = 'Owner Admin Dashboard'
admin.site.site_title = 'Restaurant Management System'