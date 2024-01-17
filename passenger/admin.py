from django.contrib import admin
from . import models
# Register your models here.
class PassengerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'nid_no', 'mobile_no']

    def first_name(self, obj):
        return obj.user.first_name
    
    def last_name(self, obj):
        return obj.user.last_name
    
admin.site.register(models.Passenger, PassengerAdmin)