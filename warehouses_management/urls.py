from django.urls import path

from . import views

urlpatterns = [
    path('', views.warehouses_list, name='warehouses_list'),
    path('wh<int:warehouse_id>', views.wh, name='wh'),
    path('whnew', views.whnew, name='whnew'),
    path('wh<int:warehouse_id>/del', views.whdel, name='whdel'),
    path('wh<int:warehouse_id>/workers', views.workers_list, name='workers_list'),
    path('wh<int:warehouse_id>/w<int:worker_id>', views.worker, name='worker'),
]

