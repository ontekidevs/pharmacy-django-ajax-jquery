from typing import Tuple
from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import CharField
from django.forms.fields import DateTimeField
from django.utils.translation import gettext_lazy as _




class Profile(models.Model):
    profileId = models.AutoField(primary_key=True, unique=True)
    gender = CharField(max_length=255, null=True, blank=True)
    fullname = CharField(max_length=255, null=True, blank=True)
    owner = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    ownerName=models.CharField(max_length=255, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    mobile = models.IntegerField(null=True, blank=True)
    nida = models.IntegerField(null=True, blank=True)
    kura = models.IntegerField(null=True, blank=True)
    licence = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(_("Email"), blank=True, max_length=254)
    location = models.CharField(max_length=255, null=True, blank=True)
    profileImage = models.ImageField(null=True, blank=True, editable=False, serialize=False)
    is_boss = models.BooleanField(_("Boss"), default=False)
    

    # medicine perms
    can_add_medicine= models.BooleanField(_("Can Add Medicine?"), default=False)
    can_edit_medicine= models.BooleanField(_("Can Edit Medicine?"), default=False)
    can_delete_medicine= models.BooleanField(_("Can Delete Medicine?"), default=False)

    # stock perms
    can_add_stock= models.BooleanField(_("Can Add Stock?"), default=False)
    can_edit_stock= models.BooleanField(_("Can Edit Stock?"), default=False)
    can_delete_stock= models.BooleanField(_("Can Delete Stock?"), default=False)

    # sales perms
    can_add_sales= models.BooleanField(_("Can Make Sales?"), default=False)

 
    can_delete_sales= models.BooleanField(_("Can Remove Sales?"), default=False)

    # staff perms
    can_add_salesman= models.BooleanField(_("Can Add Salesman?"), default=False)
    can_delete_salesman= models.BooleanField(_("Can Delete Salesman?"), default=False)

    can_generate_report= models.BooleanField(_("Can Print Report?"), default=False)


    def __str__(self) -> str:
        return str(self.owner)


    def save(self, *args, **kwargs):
        self.ownerName = self.owner.username
        super().save(*args, **kwargs)
        
expenses =(
    ('', '--choose type--'),
    ('office', 'office'),
    ('personal', 'personal')
)

class Expense(models.Model):
    expensesId = models.AutoField(primary_key= True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField(auto_now_add=True)
    expenseType = models.CharField(choices=expenses, max_length=255)
    expenseName = models.CharField(max_length=255)
    price = models.IntegerField()
        
    def __str__(self) -> str:
        return self.expenseName


