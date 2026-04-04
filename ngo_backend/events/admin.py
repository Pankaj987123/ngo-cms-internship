from django.contrib import admin
from .models import Event, Donation

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'location')

class DonationAdmin(admin.ModelAdmin):
    list_display = ('name', 'amount')

admin.site.register(Event, EventAdmin)
admin.site.register(Donation, DonationAdmin)