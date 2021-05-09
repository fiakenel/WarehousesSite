from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .forms import WHForm
from django.views import generic
from django.urls import reverse_lazy

from .models import *

class HomepageView(generic.TemplateView):
    template_name = 'warehouses_management/home.html'

class WarehouseListView(generic.ListView):
    model = Warehouse

#    def get_queryset(self):
#        return Warehouse.objects.all()

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
    model = Worker
    context_object_name = 'worker_list'

    def get_context_data(self, **kwargs):
        context = super(WorkerListView, self).get_context_data(**kwargs)
        context['warehouse_id'] = self.kwargs['warehouse_id']
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

class RackListView(generic.ListView):
    model = Rack
    context_object_name = 'rack_list'

    def get_context_data(self, kwargs):
        context = super(RackListView, self).get_context_data(**kwargs)
        context['warehouse_id'] = self.kwargs['warehouse_id']
        return context

class RackDetailView(generic.DetailView):
    model = Rack
    pk_url_kwarg = 'rack_id'

class RackCreate(generic.CreateView):
    model = Rack
    fields = ['max_weight', 'warehouse_id']

    def get_success_url(self):
        return reverse_lazy('rack_detail', args=[self.kwargs['warehouse_id'], Rack.objects.latest().id])

#class RackDelete(generic.DeleteView):
#    model = Rack
#    pk_url_kwarg = 'rack_id'
#
#    def 
