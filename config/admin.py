from django.contrib import admin
from . models import Stocks

# Register your models here.
@admin.register(Stocks)
class StocksAdmin(admin.ModelAdmin):
    list_display= ['StockName','Month','TransactionType','Quantity','Price']

