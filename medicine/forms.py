from django import forms
from django.forms import fields
from medicine.models import Medicine

class AddMedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = ("medicineName", "category", "genericName", "form", "discount", "sideEffect", "image")



class UpdateMedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields =  ("medicineName", "category", "genericName", "form", "discount", "sideEffect", "image")