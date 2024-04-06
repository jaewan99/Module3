from typing import Any
from django.db import models


# Create your models here.


class item(models.Model):
    item_name = models.CharField(max_length=100)
    item_price = models.DecimalField(max_digits=6, decimal_places=2)
    item_show = models.BooleanField(default=True)
    item_quantity = models.BigIntegerField()

    objects = models.Manager()

    def getId(self):
       return self.id
    def getPrice(self):
       return self.item_price
    def getName(self):
       return self.item_name
    def getShow(self):
       return self.item_show
    def getQuant(self):
       return self.item_quantity
    def __str__(self):
       return str(self.pk) + ": " + self.item_name 

class order(models.Model):
    payment = models.IntegerField()
    total_amount = models.DecimalField(max_digits=30, decimal_places=2)

    objects = models.Manager()
    def getOrderId(self):
       return self.id
    def getPayment(self):
       return self.payment
    def getTotalAmount(self):
       return self.total_amount
    def __str__(self):
       return str(self.pk) + ": " + str(self.payment) + str(self. total_amount)
    

class itemOrder(models.Model):
    item_id = models.ForeignKey(item, null=True, on_delete=models.SET_NULL)
    order_id = models.ForeignKey(order, null=True, on_delete=models.SET_NULL)
    line_total= models.DecimalField(max_digits=30, decimal_places=2)
    quantity = models.BigIntegerField()

    objects = models.Manager()

    def getitem_id(self):
       return self.item_id
    def getorder_id(self):
       return self.order_id
    def getline_total(self):
       return self.line_total
    def getquantity(self):
       return self.quantity
    def __str__(self):
       return str(self.pk)