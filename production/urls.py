from django.urls import path
from . import views

app_name = 'production'

urlpatterns = [
    path('', views.index, name='index'),
    path('records/', views.record_list, name='record_list'),
    path('records/create/', views.record_create, name='record_create'),
    path('records/<int:pk>/', views.record_detail, name='record_detail'),
    path('records/<int:pk>/edit/', views.record_edit, name='record_edit'),
    path('workers/', views.worker_summary, name='worker_summary'),
    path('machines/', views.machine_summary, name='machine_summary'),
] 