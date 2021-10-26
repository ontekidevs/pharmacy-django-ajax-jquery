from django import forms
from django.forms import fields
from django.forms.widgets import CheckboxInput, EmailInput, NumberInput, PasswordInput, Select, TextInput
from django.core.exceptions import ValidationError

from pharmaProfile.models import Profile, Expense, expenses


class AddExpenseForm(forms.ModelForm):
    expenseName = forms.CharField(required=True, widget=TextInput(attrs={'class':'form-control my-1', 'placeholder':'Name'}))
    expenseType = forms.ChoiceField(required=True, choices=expenses, widget=Select(attrs={'class':'form-control my-1', 'placeholder':'type'}))
    price = forms.IntegerField(required=True, widget=NumberInput(attrs={'class':'form-control my-1', 'placeholder':'Price'}))
    class Meta:
        model = Expense
        fields = [
            'expenseName', 'expenseType', 'price'
        ]




class RegisterSalesmanForm(forms.Form):

    """
    RegisterSalesman definition.
    TODO: 
        Define form fields here
        add user without any permission
    """
    firstName = forms.CharField(widget=TextInput(attrs={'class': 'form-control'}))
    middleName = forms.CharField(required=False, widget=TextInput(attrs={'class': 'form-control'}))
    lastName = forms.CharField(widget=TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(required=True, widget=TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=EmailInput(attrs={'class': 'form-control'}))
    nida = forms.IntegerField(widget=NumberInput(attrs={'class': 'form-control'}))
    licence = forms.IntegerField(widget=NumberInput(attrs={'class': 'form-control'}))
    kura = forms.IntegerField(widget=NumberInput(attrs={'class': 'form-control'}))
    mobileNumber = forms.IntegerField(required=True, widget=NumberInput(attrs={'class': 'form-control'}))

    def clean_mobile_number(self):
        cleaned_data = super().clean()
        phone = str(cleaned_data.get('mobileNumber'))
        if len(phone) != 10:
            raise ValidationError("phone number is invalid!!")
        return phone

    # def clean(self):
    #     cleaned_data = super().clean()
    #     mobile_number = cleaned_data.get("mobile_number")
    #     username = cleaned_data.get("username")

    #     if mobile_number and username:
    #         # Only do something if both fields are valid so far.
    #         if "help" not in subject:
    #             raise ValidationError(
    #                 ""
    #                 ""
    #             )



class PermitSalesmanForm(forms.ModelForm):
    
    """
    RegisterSalesman definition.
    TODO: 
        granting user permissions
    """
    is_boss = forms.BooleanField(required=False, widget=CheckboxInput(attrs={'class':'form-control'}), initial=False)
    can_add_medicine = forms.BooleanField(required=False, widget=CheckboxInput(attrs={'class':'form-control'}), initial=False)
    can_edit_medicine = forms.BooleanField(required=False, widget=CheckboxInput(attrs={'class':'form-control'}), initial=False)
    can_delete_medicine = forms.BooleanField(required=False, widget=CheckboxInput(attrs={'class':'form-control'}), initial=False)
    can_add_stock = forms.BooleanField(required=False, widget=CheckboxInput(attrs={'class':'form-control'}), initial=False)
    can_edit_stock = forms.BooleanField(required=False, widget=CheckboxInput(attrs={'class':'form-control'}), initial=False)
    can_delete_stock = forms.BooleanField(required=False, widget=CheckboxInput(attrs={'class':'form-control'}), initial=False)
    can_add_sales = forms.BooleanField(required=False, widget=CheckboxInput(attrs={'class':'form-control'}), initial=True)
    can_add_salesman = forms.BooleanField(required=False, widget=CheckboxInput(attrs={'class':'form-control'}), initial=False)
    can_delete_salesman = forms.BooleanField(required=False, widget=CheckboxInput(attrs={'class':'form-control'}), initial=False)
    can_generate_report = forms.BooleanField(required=False, widget=CheckboxInput(attrs={'class':'form-control'}), initial=False)
    class Meta:
        model = Profile
        fields = [
            'is_boss', 'can_add_medicine', 'can_edit_medicine', 'can_delete_medicine',  
            'can_add_stock', 'can_edit_stock', 'can_delete_stock', 'can_add_sales',
            'can_add_salesman', 'can_delete_salesman', 'can_generate_report'
        ]


class ChangePasswordForm(forms.Form):
    new_password = forms.CharField(widget=PasswordInput(attrs={'class':'form-control'}))
    new_password1 = forms.CharField(widget=PasswordInput(attrs={'class':'form-control'}))
