from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('/display', views.display, name='display'),
    path('/add', views.add_product, name='add_product'),
    path('delete/<int:product_id>', views.delete, name='delete')
]
