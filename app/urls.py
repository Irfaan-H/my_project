from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.workersList.as_view()),
    path('workersdetail/<str:pk>/',views.workersDetail.as_view())
]
    