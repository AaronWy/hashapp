from django.contrib import admin
from .models import Unhash,hashcatmode
# Register your models here.

class HashcatModeAdmin(admin.ModelAdmin):
    list_display = ('number', 'name')  
admin.site.register(Unhash)

admin.site.register(hashcatmode, HashcatModeAdmin)
