from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('data/', views.data_view, name='data_view'),
    path('trigger-data-generation/', views.trigger_data_generation, name='trigger_data_generation'),
    path('export-excel/', views.export_excel, name='export_excel'),
    path('export-pdf/', views.export_pdf, name='export_pdf'),
]