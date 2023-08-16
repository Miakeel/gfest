from django import forms
from django.contrib.auth.models import User
from django.forms import fields, widgets

from .models import Participant, Entry
import asyncio

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput())

class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ('qrcode_id', 'name', 'phone_nr')
        widgets = {
            #'qrcode_id': forms.HiddenInput()
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['name'].widget.attrs.update(autofocus='autofocus')

stands=(
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5','5'),
    ('6','6'),
    ('7','7'),
    ('8','8'),
    ('9','9'),
    ('10','10'),
    ('11','11'),
    ('12','12'),
    ('13','13'),
    ('14','14'),
    ('15','15'),
    ('16','16'),
    ('17','17'),
    ('18','18'),
    ('19','19'),
    ('20','20'),
    ('21','21'),
    ('22','22'),
    ('23','23'),
    ('24','24'),
    ('25','25'),
    ('26','26'),
    ('27','27'),
    ('28','28'),
    ('29','29'),
    ('30','30'),
    ('31','31'),
    ('32','32')

)

class EntryForm(forms.Form):
    qrcode_uuid = forms.UUIDField()
    stand=forms.ChoiceField(choices=stands)

class QrcodeEditForm(forms.Form):
    qrcode_uuid = forms.UUIDField()