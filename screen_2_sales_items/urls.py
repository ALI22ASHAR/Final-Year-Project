"""
URL Configuration for Screen 2: Sales & Items Management

This module includes URLs from both apps:
- items_management: Product CRUD, inventory management
- sales_analytics: KPIs, performance metrics, analytics
"""
from django.urls import path, include

app_name = 'screen_2'

urlpatterns = [
    # Items Management API
    path('items/', include('screen_2_sales_items.items_management.urls')),
    
    # Sales Analytics API
    path('analytics/', include('screen_2_sales_items.sales_analytics.urls')),
]
