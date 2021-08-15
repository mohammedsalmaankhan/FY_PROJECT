from django import forms
from .models import Medical, Patient, Heart, Diabetes

class PatientForm(forms.ModelForm):

    class Meta:
        model = Patient
        fields = ('id', 'name','Aadhar_num','contact_number','date_of_birth','gender','email',)

class MedicalForm(forms.ModelForm):


    class Meta:
        model = Medical
        fields = ('id', 'name','blood_group','height','weight','medical_condition1','medical_condition2','medical_condition3',)

class HeartForm(forms.ModelForm):

    class Meta:
        model = Heart
        fields = ('id', 'name','age','gender','chest_pain','blood_pressure','cholestoral','fasting_blood','restecg','max_heart','exang','old_peak','slope','ca','thal',)

class DiabetesForm(forms.ModelForm):

    class Meta:
        model = Diabetes
        fields = ('id', 'name','age','glucose','blood_pressure','skin_thickness','insulin','BMI','DiabetesPedigreeFunction',)
