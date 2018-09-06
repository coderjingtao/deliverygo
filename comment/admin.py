from django.contrib import admin

# Register your models here.
from comment.models import City,Suburb

class CityAdmin(admin.ModelAdmin):
    list_display = ('id','name','parent','state')
    ordering=('id',)
    search_fields = ('name',)

class SuburbAdmin(admin.ModelAdmin):
    list_display = ('id','name','postcode','city','good_count','bad_count')
    search_fields = ('name','city__name','postcode')

admin.site.register(City,CityAdmin)
admin.site.register(Suburb,SuburbAdmin)