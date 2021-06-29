from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse_lazy

from .models import *

class HomepageView(generic.TemplateView):
    template_name = 'warehouses_management/home.html'

class WarehouseListView(generic.ListView):
    model = Warehouse

    def get_context_data(self, **kwargs):
        context = super(WarehouseListView, self).get_context_data(**kwargs)
        context['relation_list'] = WarehouseSupplierM2M.objects.all()
        return context

class WarehouseDetailView(generic.DetailView):
    model = Warehouse
    pk_url_kwarg = 'warehouse_id'

class WarehouseCreate(generic.CreateView):
    model = Warehouse
    fields = ['address', 'area', 'supplier']

    def get_success_url(self):
        return reverse_lazy('warehouse_list')

class WarehouseUpdate(generic.UpdateView):
    model = Warehouse
    fields = ['address', 'area', 'supplier']
    pk_url_kwarg = 'warehouse_id'

    def get_success_url(self):
        return reverse_lazy('warehouse_list')

class WarehouseDelete(generic.DeleteView):
    model = Warehouse
    pk_url_kwarg = 'warehouse_id'

    def get_success_url(self):
        return reverse_lazy('warehouse_list')

class WorkerListView(generic.ListView):
    model = Worker
    context_object_name = 'worker_list'

    def get_queryset(self):
        workers = super().get_queryset()
        if self.kwargs['warehouse_id'] == 0:
            return workers
        else:
            return workers.filter(warehouse_id = self.kwargs['warehouse_id'])

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

    def get_initial(self):
        initial = super(WorkerCreate, self).get_initial()
        initial = initial.copy()
        if self.kwargs['warehouse_id'] != 0:
            initial['warehouse'] = self.kwargs['warehouse_id']
        return initial

    def get_success_url(self):
        return reverse_lazy('worker_list', args=[self.kwargs['warehouse_id']])

class WorkerUpdate(generic.UpdateView):
    model = Worker
    pk_url_kwarg = 'worker_id'
    fields = ['name', 'phone', 'wage', 'warehouse']

    def get_success_url(self):
        return reverse_lazy('worker_list', args=[self.kwargs['warehouse_id']])

class WorkerDelete(generic.DeleteView):
    model = Worker
    pk_url_kwarg = 'worker_id'

    def get_success_url(self):
        return reverse_lazy('worker_list', args=[self.kwargs['warehouse_id']])

#class RackListView(generic.ListView):
#    model = Rack
#    context_object_name = 'rack_list'
#
#    def get_queryset(self):
#        racks = super().get_queryset()
#        if self.kwargs['warehouse_id'] == 0:
#            return racks
#        else:
#            return racks.filter(warehouse_id = self.kwargs['warehouse_id'])
#
#    def get_context_data(self, **kwargs):
#        context = super(RackListView, self).get_context_data(**kwargs)
#        context['warehouse_id'] = self.kwargs['warehouse_id']
#        return context
#
#class RackDetailView(generic.DetailView):
#    model = Rack
#    pk_url_kwarg = 'rack_id'
#
#class RackCreate(generic.CreateView):
#    model = Rack
#    fields = ['max_weight', 'warehouse']
#
#    def get_initial(self):
#        initial = super(RackCreate, self).get_initial()
#        initial = initial.copy()
#        if self.kwargs['warehouse_id'] != 0:
#            initial['warehouse'] = self.kwargs['warehouse_id']
#        return initial
#
#    def get_success_url(self):
#        return reverse_lazy('rack_list', args=[self.kwargs['warehouse_id']])
#
#class RackDelete(generic.DeleteView):
#    model = Rack
#    pk_url_kwarg = 'rack_id'
#
#    def get_success_url(self):
#        return reverse_lazy('rack_list', args=[self.kwargs['warehouse_id']])

class BoxListView(generic.ListView):
    model = Box
    context_object_name = 'box_list'

    def get_queryset(self):
        boxes = super().get_queryset()
        if self.kwargs['warehouse_id'] == 0:
            return boxes
        return boxes.filter(warehouse_id = self.kwargs['warehouse_id'])

    def get_context_data(self, **kwargs):
        context = super(BoxListView, self).get_context_data(**kwargs)
        context['warehouse_id'] = self.kwargs['warehouse_id']
        context['weapon_list'] = Weapon.objects.all()
        return context

class BoxCreate(generic.CreateView):
    model = Box
    fields = ['price', 'amount', 'weapon', 'warehouse']

    def get_initial(self):
        initial = super(BoxCreate, self).get_initial()
        initial = initial.copy()
        if self.kwargs['warehouse_id'] != 0:
            initial['warehouse'] = self.kwargs['warehouse_id']
        return initial

    def get_success_url(self):
        return reverse_lazy('box_list', args=[self.kwargs['warehouse_id']])

class BoxUpdate(generic.UpdateView):
    model = Box
    fields = ['price', 'amount', 'weapon', 'warehouse']
    pk_url_kwarg = 'box_id'

    def get_success_url(self):
        return reverse_lazy('box_list', args=[self.kwargs['warehouse_id']])

class BoxDelete(generic.DeleteView):
    model = Box
    pk_url_kwarg = 'box_id'

    def get_success_url(self):
        return reverse_lazy('box_list', args=[self.kwargs['warehouse_id']])

class WeaponListView(generic.ListView):
    model = Weapon

class WeaponDetailView(generic.DetailView):
    model = Weapon
    pk_url_kwarg = 'weapon_id'

class WeaponCreate(generic.CreateView):
    model = Weapon
    fields = ['name']

    def get_success_url(self):
        return reverse_lazy('weapon_list')

class WeaponUpdate(generic.UpdateView):
    model = Weapon
    pk_url_kwarg = 'weapon_id'
    fields = ['name']

    def get_success_url(self):
        return reverse_lazy('weapon_list')

class WeaponDelete(generic.DeleteView):
    model = Weapon
    pk_url_kwarg = 'weapon_id'

    def get_success_url(self):
        return reverse_lazy('weapon_list')

class SupplierListView(generic.ListView):
    model = Supplier

class SupplierCreate(generic.CreateView):
    model = Supplier
    fields = ['name', 'country']

    def get_success_url(self):
        return reverse_lazy('supplier_list')

class SupplierUpdate(generic.UpdateView):
    model = Supplier
    pk_url_kwarg = 'supplier_id'
    fields = ['name', 'country']

    def get_success_url(self):
        return reverse_lazy('supplier_list')

class SupplierDelete(generic.DeleteView):
    model = Supplier
    pk_url_kwarg = 'supplier_id'

    def get_success_url(self):
        return reverse_lazy('supplier_list')

class CountryListView(generic.ListView):
    model = Country

class CountryCreate(generic.CreateView):
    model = Country
    fields = ['country']

    def get_success_url(self):
        return reverse_lazy('country_list')

class CountryUpdate(generic.UpdateView):
    model = Country
    fields = ['country']
    pk_url_kwarg = 'country_id'

    def get_success_url(self):
        return reverse_lazy('country_list')

class CountryDelete(generic.DeleteView):
    model = Country
    pk_url_kwarg = 'country_id'

    def get_success_url(self):
        return reverse_lazy('country_list')
