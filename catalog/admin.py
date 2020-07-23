from django.contrib import admin
from .models import Procurement, ProcurementFiles

class ProcurementFilesInline(admin.TabularInline):
    model = ProcurementFiles

class ProcurementAdmin(admin.ModelAdmin):
    inlines = [
        ProcurementFilesInline,
    ]

admin.site.register(Procurement, ProcurementAdmin)

