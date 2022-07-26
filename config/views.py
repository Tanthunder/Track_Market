from audioop import avg
from django.http import HttpResponse
from django.shortcuts import render
from config.models import Stocks
from django.views.generic import ListView , DetailView , CreateView , UpdateView ,DeleteView
from . import models
from django.db.models import Sum

def monthly_details(request):
    month='June'
    # to find unique stock names for particular month
    stock_name=Stocks.objects.filter(Month=month).order_by().values_list('StockName',flat=True).distinct()
    
    dict={}
    for i in stock_name:
        #logic for total buy amount per stock 
        totalbuy=Stocks.objects.filter(Month=month).filter(StockName=i).filter(TransactionType='B').aggregate(Total=Sum('Price'))['Total']
        
        #logic for total sell amount per stock 
        totalsell=Stocks.objects.filter(Month=month).filter(StockName=i).filter(TransactionType='Sell').aggregate(Total=Sum('Price'))['Total']
        
        if totalbuy == None:
            totalbuy=0
        if totalsell==None:
            totalsell=0

        Net = totalbuy-totalsell
        
        #Retrieve Buy Quantity
        BQ=Stocks.objects.filter(Month=month).filter(StockName=i).filter(TransactionType='B').aggregate(Total=Sum('Quantity'))['Total']
        #Retrieve Sell Quantity
        SQ=Stocks.objects.filter(Month=month).filter(StockName=i).filter(TransactionType='sell').aggregate(Total=Sum('Quantity'))['Total']
        #Handling 'None' conditions
        if BQ == None:
            BQ=0
        if SQ==None:
            SQ=0

        NetQ = BQ-SQ
        #creating dict inside dict to pass as context to template
        tempdict={i:{'Buyprice': totalbuy,'Sellprice': totalsell,'NetQ':NetQ,'Net':Net,'BuyQuant':BQ,'SellQuant':SQ}}
        dict.update(tempdict)
        
    return render(request,'monthly_details.html',{'context':dict})

def home(request):
    stock_name=Stocks.objects.order_by().values_list('StockName',flat=True).distinct()
    dict={}
    for i in stock_name:
        #logic for total buy amount per stock 
        totalbuy=Stocks.objects.filter(StockName=i).filter(TransactionType='B').aggregate(Total=Sum('Price'))['Total']
        
        #logic for total sell amount per stock 
        totalsell=Stocks.objects.filter(StockName=i).filter(TransactionType='Sell').aggregate(Total=Sum('Price'))['Total']
        
        if totalbuy == None:
            totalbuy=0
        if totalsell==None:
            totalsell=0

        Net = totalbuy-totalsell
        
        #Retrieve Buy Quantity
        BQ=Stocks.objects.filter(StockName=i).filter(TransactionType='B').aggregate(Total=Sum('Quantity'))['Total']
        #Retrieve Sell Quantity
        SQ=Stocks.objects.filter(StockName=i).filter(TransactionType='sell').aggregate(Total=Sum('Quantity'))['Total']
        #Handling 'None' conditions
        if BQ == None:
            BQ=0
        if SQ==None:
            SQ=0

        NetQ = BQ-SQ
        AvgPrice=Net/NetQ
        #creating dict inside dict to pass as context to template
        tempdict={i:{'TotalInvestment': Net,'AvgPrice': AvgPrice,'TotalQuant':NetQ}}
        dict.update(tempdict)
        
    return render(request,'home.html',{'context':dict})

class Details(DetailView):
    model=models.Stocks

def yearly_details(request):
    month=['January','February','March','April','May','June','July','August','September','October','November','December']

    dict={}
    for i in month:
        #logic for total buy amount per stock 
        totalbuy=Stocks.objects.filter(Month=i).filter(TransactionType='B').aggregate(Total=Sum('Price'))['Total']
        
        #logic for total sell amount per stock 
        totalsell=Stocks.objects.filter(Month=i).filter(TransactionType='Sell').aggregate(Total=Sum('Price'))['Total']
        
        if totalbuy == None:
            totalbuy=0
        if totalsell==None:
            totalsell=0

        Net = totalbuy-totalsell
        
        #creating dict inside dict to pass as context to template
        tempdict={i:{'Buyprice': totalbuy,'Sellprice': totalsell,'Net':Net}}
        dict.update(tempdict)
        
    return render(request,'yearly_details.html',{'context':dict})
