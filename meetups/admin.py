from django.contrib import admin
from .models import Event, Paticipants, Locations

# Register your models here.

class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']
    prepopulated_fields = {
        'slug': ('title', ),
    }
    list_filter = ('location', )


admin.site.register(Event, EventAdmin)
admin.site.register(Paticipants, )
admin.site.register(Locations)
