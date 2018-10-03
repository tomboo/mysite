from django.contrib import admin
from .models import Weight, BloodPressure


class WeightAdmin(admin.ModelAdmin):
    list_display = ('date', 'weight', 'body_fat', 'user')
    list_filter = ('user', 'date')


# Register your models here.
admin.site.register(Weight, WeightAdmin)
admin.site.register(BloodPressure)
