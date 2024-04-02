from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def m3activity1(request):
   allitems = item.objects.all()
   return render (request, 'm3activity1/m3activity1.html', {'items':allitems})

def configItem(request):
   allitems = item.objects.all()
   return render (request, 'm3activity1/configItem.html', {'items':allitems, 'pk':allitems})

def addItem(request):
   if(request.method == "POST"):
      itname = request.POST.get("itname")
      itprice = request.POST.get("itprice")
      iquantity = request.POST.get("iquantity")
      item.objects.create(item_name=itname, item_price=itprice, item_quantity = iquantity)
      return redirect('configItem')
   return render (request, 'm3activity1/addItem.html')

def updateItem(request, pk):
   oneitem = item.objects.get(id=pk)
   if(request.method == "POST"):
      itname = request.POST.get("itname")
      itprice = request.POST.get("itprice")
      ipk = request.POST.get("ipk")
      iquantity = request.POST.get("iquantity")
      changeitem = item.objects.filter(pk = ipk).update(item_name= itname, item_price = itprice, item_quantity = iquantity)
      return redirect('configItem')
   return render (request, 'm3activity1/updateItem.html', {'oneitem':oneitem})

def deleteItem(request, pk):
   if(request.method == "POST"):
      changeitem = item.objects.filter(pk = pk).update(item_show = False)
   return redirect('configItem')


def confirmOrder(request):
   if(request.method == "POST"):
       ptype = request.POST.get("payment_method")
       items = request.POST.get("complete_order")
       totamt = request.POST.get("total_amount")
       print("total amount: ", totamt, type(totamt))
      #  if totamt <= 0:
      #     return redirect('m3activity1')

       ord = order.objects.create(total_amount=totamt, payment=ptype)
       item_fixed = items[:-1]
       stuff = item_fixed.split("-")
       for it in stuff:
         values = it.split(":")
         item_obj = item.objects.get(pk=values[0])
         itprice = item_obj.getPrice()
         lt = itprice * int(values[1])

         # update item_quantity
         newQuant = item_obj.getQuant() - int(values[1])
         item_obj.item_quantity = newQuant
         item_obj.save()

         itemOrder.objects.create(item_id = item_obj, order_id = ord, line_total=lt, quantity=values[1])

   return redirect('m3activity1')


def checkOrder(request):
   allitemOrders = itemOrder.objects.all()
   allOrders = order.objects.all()
   return render (request, 'm3activity1/checkOrder.html', {'allitemOrders':allitemOrders, 'allOrders':allOrders})