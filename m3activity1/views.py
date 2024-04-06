from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def m3activity1(request):
   allitems = item.objects.all()
   return render (request, 'm3activity1/m3activity1.html', {'items':allitems, 'error':''})

def configItem(request):
   allitems = item.objects.all()
   return render (request, 'm3activity1/configItem.html', {'items':allitems, 'pk':allitems})

def addItem(request):
   if(request.method == "POST"):
      itprice = request.POST.get("itprice")
      iquantity = request.POST.get("iquantity")
      if (int(float(itprice)) <0) or (int(iquantity) <0):
         # return redirect('m3activity1', 'error':'Please input positive value/s')
         return render (request, 'm3activity1/addItem.html', {'error':'Please input positive value/s'})
      
      itname = request.POST.get("itname")
      item.objects.create(item_name=itname, item_price=itprice, item_quantity = iquantity)
      return redirect('configItem')
   return render (request, 'm3activity1/addItem.html')

def updateItem(request, pk):
   oneitem = item.objects.get(id=pk)
   if(request.method == "POST"):
      itprice = request.POST.get("itprice")
      iquantity = request.POST.get("iquantity")
      if (int(float(itprice)) <0) or (int(iquantity) <0):
         return render (request, 'm3activity1/updateItem.html', {'oneitem':oneitem, 'error':'Please input positive value/s'})

      itname = request.POST.get("itname")
      ipk = request.POST.get("ipk")
      
      changeitem = item.objects.filter(pk = ipk).update(item_name= itname, item_price = itprice, item_quantity = iquantity)
      return redirect('configItem')
   return render (request, 'm3activity1/updateItem.html', {'oneitem':oneitem})

def deleteItem(request, pk):
   if(request.method == "POST"):
      changeitem = item.objects.filter(pk = pk).update(item_show = False)
   return redirect('configItem')


def confirmOrder(request):
   item_obj = None
   if(request.method == "POST"):
      ptype = request.POST.get("payment_method")
      items = request.POST.get("complete_order")
      totamt = request.POST.get("total_amount")
      item_fixed = items[:-1]
      stuff = item_fixed.split("-")
      
      # check if there's an negative value in the quantity, if not saves the item to the item_lists
      item_lists = [] # [pk, quantity, lt (line total)]
      for it in stuff:
         values = it.split(":")
         item_obj = item.objects.get(pk=values[0])
         itprice = item_obj.getPrice()
         if values[1] == "":
            allitems = item.objects.all()
            return render (request, 'm3activity1/m3activity1.html', {'items':allitems, 'error':'Please input positive value/s'})
         elif int(values[1]) > item_obj.getQuant():
            allitems = item.objects.all()
            return render (request, 'm3activity1/m3activity1.html', {'items':allitems, 'error':'Please input lower quantity than the current quantity'})
         lt = itprice * int(values[1])
         item_lists.append([values[0], values[1], lt])

      # update item_quantity and create order and itemOrder
      ord = order.objects.create(total_amount=totamt, payment=ptype)
      for i in item_lists:
         item_obj = item.objects.get(pk=i[0])
         item_obj.item_quantity -= int(i[1])
         item_obj.save()
         itemOrder.objects.create(item_id = item_obj, order_id = ord, line_total=i[2], quantity=i[1])
      
   return redirect('m3activity1')


def checkOrder(request):
   allitemOrders = itemOrder.objects.all()
   allOrders = order.objects.all()
   return render (request, 'm3activity1/checkOrder.html', {'allitemOrders':allitemOrders, 'allOrders':allOrders})