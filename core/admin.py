from django.contrib import admin
from django.utils.safestring import mark_safe
from rangefilter.filter import DateRangeFilter

from core.models import Patient, VitalSigns, SignsRegistration, DetailSigns


# Register your models here.


class PatientAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'idNumber', 'age']
    search_fields = ['firstName', 'lastName', 'idNumber']
    ordering = ['lastName', 'firstName']


class VitalSignsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'minValue', 'maxValue']
    search_fields = ['name']
    ordering = ['name']


class DetailSignsInline(admin.TabularInline):
    model = DetailSigns
    extra = 2


class SignsRegistrationAdmin(admin.ModelAdmin):
    list_display = ['id', 'patient', 'date', 'vitals_status', 'signs_detail']
    list_filter = [('date', DateRangeFilter)]
    search_fields = ['patient']
    ordering = ['date']
    inlines = [
        DetailSignsInline,
    ]

    def signs_detail(self, obj):
        return mark_safe(obj.signs_detail())


admin.site.register(Patient, PatientAdmin)
admin.site.register(VitalSigns, VitalSignsAdmin)
admin.site.register(SignsRegistration, SignsRegistrationAdmin)