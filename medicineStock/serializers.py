from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from medicineStock.models import Stock


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'


class Get_Stock_List(APIView):
    def get(self, request):
        stock = Stock.objects.all()
        serialized = StockSerializer(stock, many=True)
        print(serialized)
        return Response(serialized.data)
