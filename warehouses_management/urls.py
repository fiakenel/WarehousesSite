from django.urls import path

from . import views

urlpatterns = [
    #homepage
    path('', views.HomepageView.as_view(), name='homepage'),
    #warehouses
    path('warehouses/', views.WarehouseListView.as_view(), name='warehouse_list'),
    #path('warehouses/<int:warehouse_id>/', views.WarehouseDetailView.as_view(), name='warehouse_detail'),
    path('warehouses/create/', views.WarehouseCreate.as_view(), name='warehouse_create'),
    path('warehouses/<int:warehouse_id>/delete/', views.WarehouseDelete.as_view(), name='warehouse_delete'),

    #workers
    path('warehouses/<int:warehouse_id>/workers/', views.WorkerListView.as_view(), name='worker_list'),
    #path('warehouses/<int:warehouse_id>/workers/<int:worker_id>/', views.WorkerDetailView.as_view(), name='worker_detail'),
    path('warehouses/<int:warehouse_id>/workers/create/', views.WorkerCreate.as_view(), name='worker_create'),
    path('warehouses/<int:warehouse_id>/workers/<int:worker_id>/delete/', views.WorkerDelete.as_view(), name='worker_delete'),

    #racks
    path('warehouses/<int:warehouse_id>/racks/', views.RackListView.as_view(), name='rack_list'),
    #path('warehouses/<int:warehouse_id>/racks/<int:rack_id>/', views.RackDetailView.as_view(), name='rack_detail'),
    path('warehouses/<int:warehouse_id>/racks/create/', views.RackCreate.as_view(), name='rack_create'),
    path('warehouses/<int:warehouse_id>/racks/<int:rack_id>/delete/', views.RackDelete.as_view(), name='rack_delete'),

    #box
    path('warehouses/<int:warehouse_id>/racks/<int:rack_id>/boxes/', views.BoxListView.as_view(), name='box_list'),
    #path('warehouses/<int:warehouse_id>/racks/<int:rack_id>/boxes/<int:box_id>/', views.BoxDetailView.as_view(), name='box_detail'),
    path('warehouses/<int:warehouse_id>/racks/<int:rack_id>/boxes/create/', views.BoxCreate.as_view(), name='box_create'),
    path('warehouses/<int:warehouse_id>/racks/<int:rack_id>/boxes/<int:box_id>/delete/', views.BoxDelete.as_view(), name='box_delete'),

    path('weapons/', views.WeaponListView.as_view(), name='weapon_list'),
    #path('weapons/<int:weapon_id>/', views.WeaponDetailView.as_view(), name='weapon_detail'),
    path('weapons/create/', views.WeaponCreate.as_view(), name='weapon_create'),
    path('weapons/<int:weapon_id>/delete/', views.WeaponDelete.as_view(), name='weapon_delete'),

]

