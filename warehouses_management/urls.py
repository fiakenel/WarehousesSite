from django.urls import path

from . import views

urlpatterns = [
    path('', views.whlist, name='whlist'),
    path('wh<int:warehouse_id>', views.warehouse, name='warehouse'),
]

