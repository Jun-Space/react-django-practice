from django.urls import path
from .views import accounts_list, account_detail, account_update, account_delete, account_create

urlpatterns = [
    path('list/', accounts_list, name='account_list'),
    path('detail/<str:pk>', account_detail, name='account_detail'),
    path('update/<str:pk>', account_update, name='account_update'),
    path('delete/<str:pk>', account_delete, name='account_delete'),
    path('create/', account_create, name='account_create'),

]
