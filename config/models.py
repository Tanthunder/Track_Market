from django.db import models

class Stocks(models.Model):
    StockName = models.CharField(max_length=50)
    Month = models.CharField(max_length=20)
    TransactionType = models.CharField(max_length=10)
    Quantity = models.IntegerField()
    Price = models.FloatField()

    def __str__(self):
        return self.StockName