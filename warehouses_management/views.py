from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .forms import WHForm
from django.views import generic
from django.urls import reverse_lazy

from .models import Warehouse, Worker

class WarehousesListView(generic.ListView):
    template_name = 'warehouses_management/warehouses_list.html'

    def get_queryset(self):
        return Warehouse.objects.all()

#def warehouses_list(request):
#    warehouses_list = Warehouse.objects.all()
#    context = { 'warehouses_list': warehouses_list }
#    return render(request, 'warehouses_management/warehouses_list.html', context)

class WarehouseView(generic.DetailView):
    template_name = 'warehouses_management/wh.html'
    model = Warehouse

#def wh(request, warehouse_id):
#    warehouse = get_object_or_404(Warehouse, pk=warehouse_id)
#    return render(request, 'warehouses_management/wh.html', {'warehouse':warehouse})

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
            return HttpResponseRedirect(f'/whapp/warehouses_management/{warehouse.id}')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = WHForm()
    return render(request, 'warehouses_management/whnew.html', {'form': form})

def whdel(request, warehouse_id):
    warehouse = get_object_or_404(Warehouse, pk=warehouse_id)
    warehouse.delete()
    return HttpResponseRedirect('/warehouses')

class WorkersListView(generic.ListView):
    template_name = 'warehouses_management/workers_list.html'
    context_object_name = 'workers'

    def get_queryset(self):
        context = {
            'warehouse_id': self.kwargs['warehouse_id'],
            'list': Worker.objects.filter(warehouse=self.kwargs['warehouse_id']),
        }
        return context

#def workers_list(request, warehouse_id):
#    workers_list = Worker.objects.filter(warehouse=warehouse_id)
#    context = {
#        'workers_list': workers_list,
#        'warehouse_id': warehouse_id,
#               }
#    return render(request, 'warehouses_management/workers_list.html', context)

class WorkerView(generic.DetailView):
    model = Worker
    template_name = 'warehouses_management/worker.html'

#def worker(request, warehouse_id, worker_id):
#    context = {
#        'worker': get_object_or_404(Worker, pk=worker_id),
#              }
#    return render(request, 'warehouses_management/worker.html', context)

class CreateWorkerView(generic.CreateView):
    model = Worker
    template_name = 'warehouses_management/create_worker.html'
    fields = ['name', 'phone', 'wage', 'warehouse']

    def get_success_url(self):
        return reverse_lazy('worker', args=[self.kwargs['warehouse_id'], Worker.objects.latest().id])

class DeleteWorkerView(generic.DeleteView):
    model = Worker

    def get_success_url(self):
        return reverse_lazy('workers_list', args=[self.kwargs['warehouse_id']])

