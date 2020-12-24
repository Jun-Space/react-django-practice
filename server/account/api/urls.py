from django.urls import path
from .views import accounts_rc, accounts_rud

urlpatterns = [
    path('', accounts_rc, name='account_list_create'),
    path('/', accounts_rc, name='account_list_create'),
    path('/<str:pk>', accounts_rud, name='account_retrieve_update_destroy'),
    path('/<str:pk>/', accounts_rud, name='account_retrieve_update_destroy'),

]
