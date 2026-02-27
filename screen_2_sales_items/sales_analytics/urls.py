from django.urls import path
from . import views

app_name = 'sales_analytics'

urlpatterns = [
    # KPIs for top cards
    path('kpis/', views.sales_kpis, name='sales-kpis'),
    
    # Monthly performance chart
    path('monthly-performance/', views.monthly_performance, name='monthly-performance'),
    
    # Category breakdown
    path('category-breakdown/', views.category_breakdown, name='category-breakdown'),
    
    # Top products
    path('top-products/', views.top_products, name='top-products'),
    
    # Sales trends
    path('trends/', views.sales_trends, name='sales-trends'),
    
    # Sales targets
    path('targets/', views.sales_targets, name='sales-targets'),
]
