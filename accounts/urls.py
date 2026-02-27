from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.account_list, name='account-list'),
    path('<int:pk>/', views.account_detail, name='account-detail'),
]
