from django.http.response import HttpResponse, JsonResponse
from django.views import generic
from medicine.models import Medicine
from medicineStock.models import Stock


class SaleView(generic.TemplateView):

    template_name= "sales/sales.html"
    
    def get_context_data(self, **kwargs):
        context = super(SaleView, self).get_context_data(**kwargs)
        context['stock'] = Stock.objects.all()
        return context



def GetMedicine(request, pk):
    print(pk)
    medicine = Medicine.objects.filter(medicineName=pk).first()
    stock = Stock.objects.filter(medicineId=medicine.pk).values('quantity', 'sellingPrice')
    return JsonResponse({'stock': list(stock)}, status=200)
    