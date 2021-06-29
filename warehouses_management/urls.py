from django.urls import path

from . import views

urlpatterns = [
    #homepage
    path('', views.HomepageView.as_view(), name='homepage'),
    #warehouses
    path('warehouses/', views.WarehouseListView.as_view(), name='warehouse_list'),
    path('warehouses/<int:warehouse_id>/update/', views.WarehouseUpdate.as_view(), name='warehouse_update'),
    path('warehouses/create/', views.WarehouseCreate.as_view(), name='warehouse_create'),
    path('warehouses/<int:warehouse_id>/delete/', views.WarehouseDelete.as_view(), name='warehouse_delete'),

    #workers
    path('warehouses/<int:warehouse_id>/workers/', views.WorkerListView.as_view(), name='worker_list'),
    path('warehouses/<int:warehouse_id>/workers/<int:worker_id>/update', views.WorkerUpdate.as_view(), name='worker_update'),
    path('warehouses/<int:warehouse_id>/workers/create/', views.WorkerCreate.as_view(), name='worker_create'),
    path('warehouses/<int:warehouse_id>/workers/<int:worker_id>/delete/', views.WorkerDelete.as_view(), name='worker_delete'),

#    #racks
#    path('warehouses/<int:warehouse_id>/racks/', views.RackListView.as_view(), name='rack_list'),
#    #path('warehouses/<int:warehouse_id>/racks/<int:rack_id>/', views.RackDetailView.as_view(), name='rack_detail'),
#    path('warehouses/<int:warehouse_id>/racks/create/', views.RackCreate.as_view(), name='rack_create'),
#    path('warehouses/<int:warehouse_id>/racks/<int:rack_id>/delete/', views.RackDelete.as_view(), name='rack_delete'),

    #box
    path('warehouses/<int:warehouse_id>/boxes/', views.BoxListView.as_view(), name='box_list'),
    path('warehouses/<int:warehouse_id>/boxes/<int:box_id>/update/', views.BoxUpdate.as_view(), name='box_update'),
    path('warehouses/<int:warehouse_id>/boxes/create/', views.BoxCreate.as_view(), name='box_create'),
    path('warehouses/<int:warehouse_id>/boxes/<int:box_id>/delete/', views.BoxDelete.as_view(), name='box_delete'),

    #weapon
    path('weapons/', views.WeaponListView.as_view(), name='weapon_list'),
    path('weapons/<int:weapon_id>/update', views.WeaponUpdate.as_view(), name='weapon_update'),
    path('weapons/create/', views.WeaponCreate.as_view(), name='weapon_create'),
    path('weapons/<int:weapon_id>/delete/', views.WeaponDelete.as_view(), name='weapon_delete'),

    #suppliers
    path('suppliers/', views.SupplierListView.as_view(), name='supplier_list'),
    path('suppliers/<int:supplier_id>/update', views.SupplierUpdate.as_view(), name='supplier_update'),
    path('suppliers/create/', views.SupplierCreate.as_view(), name='supplier_create'),
    path('suppliers/<int:supplier_id>/delete/', views.SupplierDelete.as_view(), name='supplier_delete'),

    #countries
    path('countries/', views.CountryListView.as_view(), name='country_list'),
    path('countries/<int:country_id>/update', views.CountryUpdate.as_view(), name='country_update'),
    path('countries/create/', views.CountryCreate.as_view(), name='country_create'),
    path('countries/<int:country_id>/delete/', views.CountryDelete.as_view(), name='country_delete'),
]

