from django.urls import path
from . import views

urlpatterns = [
    
    path('workers/',views.workersList.as_view())
]
    