from django.urls import path
from pharmaProfile import views as userViews


urlpatterns = [
    path('', userViews.SalesManRegisterView.as_view(), name='add_user'),
    path('permit/', userViews.PermitSalesman.as_view(), name='permit'),
    path('users/', userViews.ManageUser.as_view(), name='users'),
    path('resete-password/<int:pk>/', userViews.resetePassword, name='resete_password'),
    path('remove-user/<int:pk>/', userViews.RemoveUser, name='remove_user'),
    path('change-password/', userViews.changePassword, name='change_password'),
    path('get-user/<int:pk>/', userViews.GetUser, name='get_user'),
    path('expanses/', userViews.Expenses.as_view(), name='expenses'),
]
