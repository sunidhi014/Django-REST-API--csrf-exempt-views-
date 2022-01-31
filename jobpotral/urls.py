from django.contrib import admin
from django.urls import path, include
from . views import job_list, job_detail

urlpatterns = [
    path('job/', job_list, name='job_list'),
    path('detail/<int:pk>/', job_detail, name='job_detail'),
    path('job/<int:pk>/', job_detail, name='job_detail'),
]