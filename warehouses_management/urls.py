from django.urls import path

from . import views

urlpatterns = [
    #warehouses
    path('warehouses/', views.WarehouseListView.as_view(), name='warehouse_list'),
    path('warehouses/<int:warehouse_id>/', views.WarehouseDetailView.as_view(), name='warehouse_detail'),
    path('warehouses/create/', views.WarehouseCreate.as_view(), name='warehouse_create'),
    path('warehouses/<int:warehouse_id>/delete/', views.WarehouseDelete.as_view(), name='warehouse_delete'),

    #workers
    path('warehouses/<int:warehouse_id>/workers/', views.WorkerListView.as_view(), name='worker_list'),
    path('warehouses/<int:warehouse_id>/workers/<int:worker_id>/', views.WorkerDetailView.as_view(), name='worker_detail'),
    path('warehouses/<int:warehouse_id>/workers/create/', views.WorkerCreate.as_view(), name='worker_create'),
    path('warehouses/<int:warehouse_id>/workers/<int:worker_id>/delete/', views.WorkerDelete.as_view(), name='delete_worker'),
]

