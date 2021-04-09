from django.urls import path

from . import views

urlpatterns = [
    #warehouses
    path('warehouses/', views.WarehousesListView.as_view(), name='warehouses_list'),
    path('warehouses/<int:pk>/', views.WarehouseView.as_view(), name='wh'),
    path('warehouses/whnew/', views.whnew, name='whnew'),

    #workers
    path('warehouses/<int:warehouse_id>/del/', views.whdel, name='whdel'),
    path('warehouses/<int:warehouse_id>/workers/', views.WorkersListView.as_view(), name='workers_list'),
    path('warehouses/<int:warehouse_id>/<int:pk>/', views.WorkerView.as_view(), name='worker'),
    path('warehouses/<int:warehouse_id>/wnew/', views.WorkerCreateView.as_view(), name='wnew'),
]

