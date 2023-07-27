from django import forms
from .models import ModelPatient, ModelVisit

class FormPatient(forms.ModelForm):
    dob = forms.DateField(widget=forms.NumberInput(attrs={'type': 'date'}))
    CHOICES = [('Male', 'Male'), ('Female', 'Female')]
    gender = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
    class Meta:
        model = ModelPatient
        exclude = ['doctor']


class FormVisit(forms.ModelForm):
    CHOICES = [('Skin Disease', 'Skin Disease'), ('Heart Disease', 'Heart Disease'), ('Corona', 'Corona')]
    disease = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)

    PILLS = [('Some_Micin', 'Some_Micin'), ('One_Cetamol', 'One_Cetamol'), ('Take_Isprin', 'Take_Isprin'), ('WhiteGel', 'WhiteGel')]
    medicine = forms.MultipleChoiceField(required=False, widget=forms.CheckboxSelectMultiple, choices=PILLS)
    
    TESTS = [('Extra_Metry', 'Extra_Metry'), ('Some_Tropy', 'Some_Tropy'), ('This_Plasty', 'This_Plasty'), ('One_Chinasis', 'One_Chinasis')]
    tests = forms.MultipleChoiceField(required=False, widget=forms.CheckboxSelectMultiple, choices=TESTS)
    # report_ready = forms.BooleanField(required=False)
    
    class Meta:
        model = ModelVisit
        exclude = ['date', 'follow_up', 'charges', 'doctor', 'report', 'report_ready']

        