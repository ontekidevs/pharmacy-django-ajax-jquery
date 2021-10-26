from django import forms
from django.forms import fields
from medicineStock.models import Stock


class AddStockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields =(
            'medicineId', 'expireDate', 'quantity', 
            'buyingPrice', 'sellingPrice'
            )


class EditStockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields =(
            'medicineId', 'expireDate', 
            'buyingPrice', 'sellingPrice',
            )
    



class UpdateStockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields =(
            'expireDate', 'quantity', 
            'buyingPrice', 'sellingPrice',
            )




class AddNewStockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields =(
            'medicineId', 'expireDate', 'quantity', 
            'buyingPrice', 'sellingPrice',
            )
        