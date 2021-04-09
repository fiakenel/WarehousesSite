from django.urls import path

from . import views

urlpatterns = [
    path('warehouses', views.warehouses_list, name='warehouses_list'),
    path('warehouses/wh<int:warehouse_id>', views.wh, name='wh'),
    path('warehouses/whnew', views.whnew, name='whnew'),
    path('warehouses/wh<int:warehouse_id>/del', views.whdel, name='whdel'),
    path('warehouses/wh<int:warehouse_id>/workers', views.workers_list, name='workers_list'),
    path('warehouses/wh<int:warehouse_id>/w<int:worker_id>', views.worker, name='worker'),
    #path('warehouses/wh<int:warehouse_id>/wnew', views.wo
]

