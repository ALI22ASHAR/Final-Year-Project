"""
Dashboard URL Configuration
============================

All dashboard API endpoints for analytics and reporting
"""

from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    # Main KPIs endpoint - Returns all primary KPIs
    path('kpis/', views.dashboard_kpis, name='kpis'),
    
    # Monthly revenue breakdown
    path('monthly-revenue/', views.monthly_revenue, name='monthly-revenue'),
    
    # Top selling products
    path('top-products/', views.top_products, name='top-products'),
    
    # Low stock alerts
    path('low-stock-products/', views.low_stock_products, name='low-stock-products'),
    
    # Recent sales transactions
    path('recent-sales/', views.recent_sales, name='recent-sales'),
    
    # Outstanding invoices
    path('outstanding-invoices/', views.outstanding_invoices, name='outstanding-invoices'),
    
    # Sales performance over time
    path('sales-performance/', views.sales_performance, name='sales-performance'),
]
