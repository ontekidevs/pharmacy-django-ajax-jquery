from django.db.models.signals import post_save
from django.dispatch import receiver
from medicineStock.models import Stock, Purchase

@receiver(post_save, sender = Stock)
def post_save_created_farmer(sender, instance, created, **kwargs):
    if created:
        Purchase.objects.create(
            stockName =instance.medicineId, 
            buyingPrice = instance.buyingPrice,
            addedBy= instance.addedBy,
            quantity= instance.quantity,
            expireDate = instance.expireDate,
            sellingPrice= instance.sellingPrice,
            )
            