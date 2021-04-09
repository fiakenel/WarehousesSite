from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from .models import Warehouse, Worker
from .forms import WHForm

def warehouses_list(request):
    warehouses_list = Warehouse.objects.all()
    context = { 'warehouses_list': warehouses_list }
    return render(request, 'warehouses/warehouses_list.html', context)

def wh(request, warehouse_id):
    warehouse = get_object_or_404(Warehouse, pk=warehouse_id)
    return render(request, 'warehouses/wh.html', {'warehouse':warehouse})

def whnew(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = WHForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            warehouse = Warehouse(address=form.cleaned_data['address'],
                                  area=form.cleaned_data['area'])
            warehouse.save()
            # redirect to a new URL:
            return HttpResponseRedirect('wh' + str(warehouse.id))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = WHForm()
    return render(request, 'warehouses/whnew.html', {'form': form})

def whdel(request, warehouse_id):
    warehouse = get_object_or_404(Warehouse, pk=warehouse_id)
    warehouse.delete()
    return HttpResponseRedirect('/warehouses')

def workers_list(request, warehouse_id):
    workers_list = Worker.objects.filter(warehouse=warehouse_id)
    context = {
        'workers_list': workers_list,
        'warehouse_id': warehouse_id,
               }
    return render(request, 'warehouses/workers_list.html', context)

def worker(request, warehouse_id, worker_id):
    context = {
        'worker': get_object_or_404(Worker, pk=worker_id),
              }
    return render(request, 'warehouses/worker.html', context)
