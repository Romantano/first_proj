from django.contrib import admin
from .models import Period, ChangeBalance


# Register your models here.

class PeriodAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'start_day', 'end_day', 'description')


class ChangeBalanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'period', 'date', 'sum', 'name', 'change')


admin.site.register(Period, PeriodAdmin)
admin.site.register(ChangeBalance, ChangeBalanceAdmin)
