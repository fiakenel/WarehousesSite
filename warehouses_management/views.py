from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Warehouses

def whlist(request):
    warehouses_list = Warehouses.objects.all()
    context = { 'warehouses_list': warehouses_list }
    return render(request, 'warehouses/whlist.html', context)

def warehouse(request, warehouse_id):
    return HttpResponse("IT WORKS!!!")
