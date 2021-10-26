from datetime import date
from json import dumps
from django.forms.models import model_to_dict
from django.http.response import HttpResponse, JsonResponse
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, get_list_or_404, redirect
from medicineStock.forms import *
from medicineStock.models import Stock
from django.views import generic



class CreateStock(generic.TemplateView):
    # template_name= 'templates.html'
    template_name= 'stock/dashboard.html'


class StockView(generic.ListView):
    template_name = "stock/stock.html"
    model = Stock
    context_object_name= 'stocks'


    
    def get_context_data(self, **kwargs):
        context = super(StockView, self).get_context_data(**kwargs)
        expired = []
        expired_total = 0
        soon_expired_total = 0
        safe_total = 0
        soon_expired = []
        safe = []

        both = self.model.objects.all()
        for  sto in both:
            if sto.expired:
                expired.append(sto)
                expired_total+=1
                continue
            elif sto.soonexpired:
                soon_expired_total+=1
                soon_expired.append(sto)
                continue
            else:
                safe_total+=1
                safe.append(sto)
                continue
        
        context['total']= self.model.objects.all().count()
        context['expired']= expired_total
        context['soon_expired']= soon_expired_total
        context['safe']= safe_total

        return context


def StockFilter(request):
    import datetime
    today =  datetime.date.today()
    if request.GET['keyword']=='expired':
        if request.is_ajax():
            filtered  = Stock.objects.filter(expireDate__lte=today).values()
            return JsonResponse({'data': list(filtered)})


    if request.GET['keyword']=='soon_expired':
        dayz= datetime.date.today() + datetime.timedelta(days=5)
        if request.is_ajax():
            filtered = Stock.objects.filter(expireDate__lte=dayz, expireDate__gt=today).values()
            return JsonResponse({'data': list(filtered)})


    if request.GET['keyword']=='safe':
        dayz= datetime.date.today() + datetime.timedelta(days=5)
        if request.is_ajax():
            filtered = Stock.objects.filter(expireDate__gte=dayz).values()
            print(filtered)
            return JsonResponse({'data': dumps(filtered)})



    if request.GET['keyword']=='all':
        if request.is_ajax():
            filtered  = Stock.objects.all().values()
            return JsonResponse({'data': list(filtered)})

    return HttpResponse('wrong request')


def deleteStock(request, pk):
    Stock.objects.get(id=pk).delete()
    return redirect('allstock')

class EditStock(generic.UpdateView):
    template_name = 'stock/edit_stock.html'
    model = Stock
    form_class = EditStockForm
    success_url = reverse_lazy('allstock')


class UpdateExistStock(generic.UpdateView):
    template_name = 'stock/edit_stock.html'
    model = Stock
    form_class = UpdateStockForm
    success_url = reverse_lazy('allstock')
    

class AdddNewStock(generic.UpdateView):
    template_name = 'stock/edit_stock.html'
    model = Stock
    form_class = AddNewStockForm
    success_url = reverse_lazy('allstock')
    