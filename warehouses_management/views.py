from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .forms import WHForm
from django.views import generic
from django.urls import reverse_lazy

from .models import Warehouse, Worker

class WarehouseListView(generic.ListView):

    def get_queryset(self):
        return Warehouse.objects.all()

class WarehouseDetailView(generic.DetailView):
    model = Warehouse
    pk_url_kwarg = 'warehouse_id'

class WarehouseCreate(generic.CreateView):
    model = Warehouse
    fields = ['address', 'area']

    def get_success_url(self):
        return reverse_lazy('warehouse_detail', args=[Warehouse.objects.latest().id])

class WarehouseDelete(generic.DeleteView):
    model = Warehouse
    pk_url_kwarg = 'warehouse_id'

    def get_success_url(self):
        return reverse_lazy('warehouse_list')

class WorkerListView(generic.ListView):
    context_object_name = 'workers'

    def get_queryset(self):
        context = {
            'warehouse_id': self.kwargs['warehouse_id'],
            'list': Worker.objects.filter(warehouse=self.kwargs['warehouse_id']),
        }
        return context

class WorkerDetailView(generic.DetailView):
    model = Worker
    pk_url_kwarg = 'worker_id'

class WorkerCreate(generic.CreateView):
    model = Worker
    fields = ['name', 'phone', 'wage', 'warehouse']

    def get_success_url(self):
        return reverse_lazy('worker_detail', args=[self.kwargs['warehouse_id'], Worker.objects.latest().id])

class WorkerDelete(generic.DeleteView):
    model = Worker
    pk_url_kwarg = 'worker_id'

    def get_success_url(self):
        return reverse_lazy('worker_list', args=[self.kwargs['warehouse_id']])
