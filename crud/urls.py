from django.urls import path
from .views import StudentListView, StudentCreateView, StudentDeleteView, StudentUpdateView, StudentDetailView

urlpatterns = [

    path('', StudentListView.as_view(), name = 'base'),
    path('create-student/', StudentCreateView.as_view(), name = 's_create'),
    path('st-delete/<int:pk>/', StudentDeleteView.as_view(), name = 's_delete'),
    path('st-update/<int:pk>/', StudentUpdateView.as_view(), name = 's_update'),
    path('st-detail/<int:pk>/', StudentDetailView.as_view(), name = 's_detail'),
    
]   