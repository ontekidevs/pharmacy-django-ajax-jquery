from django.db import models
import datetime
from django.contrib.auth.models import User


class Stock(models.Model):
    stockId = models.AutoField(primary_key= True)
    medicineId = models.ForeignKey('medicine.Medicine', on_delete=models.CASCADE, null=True, blank=True)
    stockName = models.CharField(max_length=255, null=True, blank=True)
    expireDate = models.DateField(blank=True, null=True)
    tako = models.CharField(max_length=255, null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    buyingPrice = models.IntegerField(null=True, blank=True)
    _profit = models.IntegerField(null=True, blank=True)
    sellingPrice = models.IntegerField(null=True, blank=True)
    addedBy = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self) -> str:
        return str(self.medicineId)
    
    def save(self, *args, **kwargs):
        self.stockName=self.medicineId.medicineName
        self._profit = self.profit
        super().save(*args, **kwargs)

    @property
    def profit(self):
        profit = ((self.sellingPrice - self.buyingPrice)/self.buyingPrice)*100
        profit = round(profit, 2)
        return profit
            


    
    @property
    def expired(self):
        exp = self.expireDate
        today =  datetime.date.today()
        if exp <= today:
            return True
        
        else:
            return False

    @property
    def soonexpired(self):
        diff = self.expireDate - datetime.date.today()
        if ((diff.days) <= 5) and ((diff.days) > 0):
            return True        
        else:
            return False


class Purchase(models.Model):
    purcahaseId = models.AutoField(primary_key= True)
    stockName = models.CharField(max_length=255, null=True, blank=True)
    dueDate = models.DateField(auto_now_add=True, null=True, blank=True)
    sellingPrice = models.IntegerField(null=True, blank=True)
    buyingPrice = models.IntegerField(null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    expireDate = models.DateField(blank=True, null=True)
    addedBy = models.CharField(max_length=255, null=True, blank=True)
        
    def __str__(self) -> str:
        return self.stockName
