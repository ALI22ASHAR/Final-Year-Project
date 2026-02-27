from django.urls import path
from . import views

app_name = 'invoices'

urlpatterns = [
    path('', views.invoice_list, name='invoice-list'),
    path('<int:pk>/', views.invoice_detail, name='invoice-detail'),
]
