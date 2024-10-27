from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Patients


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class NameForm(forms.Form):
    your_name = forms.CharField(label="Your name", max_length=100)


class ScoreForm(forms.ModelForm):
    class Meta:
        model = Patients
        fields = ['name', 'years']


class PreeclampsiaForm(forms.ModelForm):
    class Meta:
        model = Patients
        # fields = ['patient_id', 'name', 'years', 'probe_date', 'birth_date', 'arterial_pressure', 'gw', 'baby_weight',
        #           'erythrocytes', 'hemoglobin']
        fields = ['patient_id', 'name', 'years', 'probe_date', 'birth_date', 'arterial_pressure', 'gw', 'baby_weight',
                  'erythrocytes', 'hemoglobin']

