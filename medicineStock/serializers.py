from django.db import models
from rest_framework import fields, serializers
from medicineStock.models import Stock
from medicine.models import Medicine
from rest_framework.generics import APIView


class StockSerializer(serializers.ModelSerializer):
    model= Stock 
    fields= '__all__'

class FilteredStock(APIView):
    def post(self, request, formart=None):
    
        pass