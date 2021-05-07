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

class WarehouseCreate(generic.CreateView):
    model = Warehouse
    fields = ['address', 'area']

    def get_success_url(self):
        return reverse_lazy('wh', args=[Warehouse.objects.latest().id])

#class WarehouseDelete(generic.DeleteView):
#    model = Warehouse
#    pk_url_kwarg = 'warehouse_id'
#
#    def get_success_url(self):
#        return reverse_lazy('warehouses_list')

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

class WorkerView(generic.DetailView):
    model = Worker
    template_name = 'warehouses_management/worker.html'

class CreateWorkerView(generic.CreateView):
    model = Worker
    template_name = 'warehouses_management/create_worker.html'
    fields = ['name', 'phone', 'wage', 'warehouse']

    def get_success_url(self):
        return reverse_lazy('worker', args=[self.kwargs['warehouse_id'], Worker.objects.latest().id])

class DeleteWorkerView(generic.DeleteView):
    model = Worker
    pk_url_kwarg = 'worker_id'

    def get_success_url(self):
        return reverse_lazy('workers_list', args=[self.kwargs['warehouse_id']])
