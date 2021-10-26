from django.urls import path
from medicineStock import views as stockViews

urlpatterns = [
    path('', stockViews.CreateStock.as_view(), name='dashboard'),
    path('stock/', stockViews.StockView.as_view(), name='allstock'),
    path('delete-stock/<int:pk>/', stockViews.deleteStock, name='delete_stock'),
    path('edit-stock/<int:pk>/', stockViews.EditStock.as_view(), name='edit_stock'),
    path('update-exist-stock/<int:pk>/', stockViews.UpdateExistStock.as_view(), name='add_stock'),
    path('add-new-stock/', stockViews.AdddNewStock.as_view(), name='add_stock'),
    path('filter/', stockViews.StockFilter, name='filter'),
]