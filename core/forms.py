from captcha.fields import CaptchaField
from django import forms


class DataQueryForm(forms.Form):
    idNumber = forms.IntegerField(label='Id Number')
    age = forms.IntegerField()
    captcha = CaptchaField()
