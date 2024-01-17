from django.contrib import admin
from . import models

# Register your models here.
class TrainAdmin(admin.ModelAdmin):
   prepopulated_fields = {'slug':('name',)}

class StationAdmin(admin.ModelAdmin):
   prepopulated_fields = {'slug':('name',)}
                 
admin.site.register(models.Train, TrainAdmin)
admin.site.register(models.Station, StationAdmin)
admin.site.register(models.Review)