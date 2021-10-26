from django.db import models
from django.contrib.auth.models import User


class Sale(models.Model):
    saleId = models.AutoField(primary_key= True)
    medicineId = models.ForeignKey('medicine.Medicine', on_delete=models.CASCADE, null=True, blank=True)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    dueDate = models.DateField()
    quantity = models.IntegerField()
    paymentId = models.ForeignKey('Payment', on_delete=models.CASCADE, null=True, blank=True)
    sellingPrice = models.IntegerField()
        
    def __str__(self) -> str:
        return str(self.medicine_id)

class ModeOfPayment(models.Model):
    mopId = models.AutoField(primary_key= True)
    modeOfPayment = models.CharField(max_length=255)
        
    def __str__(self) -> str:
        return self.mode_of_payment

status = (
    ('payed', 'payed'),
    ('not_payed', 'not payed'),
)

class Payment(models.Model):
    paymentId = models.AutoField(primary_key= True)
    modeOfPayment = models.ForeignKey('ModeOfPayment', on_delete=models.CASCADE, null=True, blank=True)
    amount = models.IntegerField()
    dueDate = models.DateField()
    NHIFNumber = models.CharField(max_length=255)
    status = models.CharField(choices=status ,max_length=255)
        
    def __str__(self) -> str:
        return str(self.modeOfPayment)

