
from django.urls import path
from . import views


app_name = 'records'
urlpatterns = [
    path('', views.record, name='record'),
    path('<int:pk>/', views.diary, name='diary'),
    path('write/', views.write, name='write'),
    path('success/', views.success, name='success'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/edit', views.edit, name = 'edit'),
    path('<int:pk>/update', views.update, name = 'update'),
]
