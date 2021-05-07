from django.urls import path

from . import views

urlpatterns = [
    #warehouses
    path('warehouses/', views.WarehousesListView.as_view(), name='warehouse_list'),
    path('warehouses/<int:warehouse_id>/', views.WarehouseDetailView.as_view(), name='warehouse_detail'),
    path('warehouses/create/', views.WarehouseCreate.as_view(), name='warehouse_create'),
    path('warehouses/<int:warehouse_id>/delete/', views.WarehouseDelete.as_view(), name='warehouse_delete'),

    #workers
    path('warehouses/<int:warehouse_id>/workers/', views.WorkersListView.as_view(), name='workers_list'),
    path('warehouses/<int:warehouse_id>/workers/<int:pk>/', views.WorkerView.as_view(), name='worker'),
    path('warehouses/<int:warehouse_id>/workers/create-worker/', views.CreateWorkerView.as_view(), name='create_worker'),
    path('warehouses/<int:warehouse_id>/workers/<int:worker_id>/delete/', views.DeleteWorkerView.as_view(), name='delete_worker'),
]

