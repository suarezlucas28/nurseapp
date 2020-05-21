from django.db import models

# Create your models here.
from django.db.models import CASCADE
from django.utils import timezone


class Patient(models.Model):
    firstName = models.CharField(max_length=20, verbose_name="First Name")
    lastName = models.CharField(max_length=20, verbose_name="Last Name")
    idNumber = models.PositiveIntegerField(verbose_name="ID Number")
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.lastName + ' ' + self.firstName + ' (' + str(self.idNumber) + ')'

    def name(self):
        return self.lastName + ', ' + self.firstName


class VitalSigns(models.Model):
    name = models.CharField(max_length=20)
    minValue = models.IntegerField(verbose_name="Min Value")
    maxValue = models.IntegerField(verbose_name="Min Value")

    class Meta:
        verbose_name = 'Vital Sign'
        verbose_name_plural = 'Vital Signs'

    def __str__(self):
        return self.name


class SignsRegistration(models.Model):
    patient = models.ForeignKey(Patient, on_delete=CASCADE)
    date = models.DateField(default=timezone.now())

    class Meta:
        verbose_name = 'Registration of Vital Sign'
        verbose_name_plural = 'Registration of Vital Signs'
        unique_together = [['patient', 'date']]

    def __str__(self):
        return self.patient.name() + ' ' + str(self.date)

    def vitals_status(self):
        status = 'Normal'
        signs = DetailSigns.objects.filter(signRegistration=self)
        for sign in signs:
            if not sign.normal_value():
                status = 'Risk'
        return status

    def signs_detail(self):
        detail = ""
        signs = DetailSigns.objects.filter(signRegistration=self)
        for sign in signs:
            if not sign.normal_value():
                detail += '<b>'+sign.vitalSigns.name+' ('+str(sign.currentValue)+'):</b> outside' \
                    ' normal value (min: '+str(sign.vitalSigns.minValue)+', max: ' + \
                    str(sign.vitalSigns.maxValue)+')<br>'
            else:
                detail += '<b>' + sign.vitalSigns.name + ' (' + str(sign.currentValue) + '):</b> inside' \
                    ' normal value (min: ' + str(sign.vitalSigns.minValue) + ', max: ' + \
                    str(sign.vitalSigns.maxValue) + ')<br>'
        return detail

    def get_blood_pressure(self):
        data = DetailSigns.objects.get(signRegistration=self, vitalSigns__name="blood pressure")
        if data:
            return data.currentValue
        else:
            return 0

    def get_heart_rate(self):
        data = DetailSigns.objects.get(signRegistration=self, vitalSigns__name="heart rate")
        if data:
            return data.currentValue
        else:
            return 0



class DetailSigns(models.Model):
    signRegistration = models.ForeignKey(SignsRegistration, on_delete=CASCADE)
    vitalSigns = models.ForeignKey(VitalSigns, on_delete=CASCADE)
    currentValue = models.IntegerField()

    class Meta:
        unique_together = [['signRegistration', 'vitalSigns']]

    def normal_value(self):
        if self.vitalSigns.minValue <= self.currentValue and self.currentValue <= self.vitalSigns.maxValue:
            return True
        else:
            return False




