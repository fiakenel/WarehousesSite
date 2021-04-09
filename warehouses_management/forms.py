from django import forms

class WHForm (forms.Form):
    address = forms.CharField(label='Адреса', max_length=100)
    area = forms.IntegerField(label='Площа')
