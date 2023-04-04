from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('best/', views.best, name = 'best'),
    path('detail/<int:pk>/', views.detail, name = 'detail'),
    path('best/write/', views.write, name = 'write'),
]

