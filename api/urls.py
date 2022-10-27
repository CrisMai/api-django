from django.contrib import admin
from django.urls import path, include
from .views import contas, conta, credito, debito, extratoAll, extrato

urlpatterns = [
    path('', contas, name="list-contas"),
    path('conta', conta, name="list-contas"),
    path('credito', credito, name="credito-conta"),
    path('debito', debito, name="debito-conta"),
    path('extratoAll', extratoAll, name="extrato-contas"),
    path('extrato/<str:query>', extrato, name="extrato-conta"),
]
