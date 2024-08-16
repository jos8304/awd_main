from django.urls import path,reverse
from . import views


urlpatterns = [
    path('stocks/', views.stocks, name='stocks'),
    path('stock-autocomplete/', views.StockAutocomplete.as_view(), name='stock_autocomplete'),
    path('stock-detail/<int:pk>/', views.stock_detail, name='stock_detail') 
         
]