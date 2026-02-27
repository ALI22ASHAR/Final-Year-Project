from django.urls import path
from . import views

app_name = 'items_management'

urlpatterns = [
    # Product CRUD
    path('products/', views.product_list_create, name='product-list-create'),
    path('products/<int:pk>/', views.product_detail, name='product-detail'),
    path('products/<int:pk>/history/', views.product_stock_history, name='product-history'),
    
    # Categories
    path('categories/', views.categories_list, name='categories-list'),
    
    # Bulk operations
    path('products/bulk-update/', views.bulk_update_stock, name='bulk-update-stock'),
    
    # Search
    path('products/search/suggestions/', views.product_search_suggestions, name='search-suggestions'),
]
