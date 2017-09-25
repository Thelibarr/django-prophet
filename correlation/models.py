from django.db import models

class StockTicker(models.Model):
    ticker=models.CharField(max_length=6)
