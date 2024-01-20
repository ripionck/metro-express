from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Train, Station, Day, Schedule, TrainReview

# Register your models here.
class TrainAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_schedule_display', 'start_station', 'end_station', 'distance')
    list_filter = ('schedule',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}

    def get_schedule_display(self, obj):
        return mark_safe(', '.join([day.name for day in obj.day_of_week.all()]))
    
    get_schedule_display.short_description = 'Schedule'

admin.site.register(Station)
admin.site.register(Day)
admin.site.register(Schedule)
admin.site.register(Train, TrainAdmin)
admin.site.register(TrainReview)

   
