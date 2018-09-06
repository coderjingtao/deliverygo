from django.contrib import admin

# Register your models here.
from risk.models import Risk, Area

class RiskAdmin(admin.ModelAdmin):
    list_display = ('id','name','level','desp')
    ordering=('id',)

class AreaAdmin(admin.ModelAdmin):
    list_display = ('id','name','risk')
    search_fields = ('name',)

admin.site.register(Risk,RiskAdmin)
admin.site.register(Area,AreaAdmin)