from django.urls import path
from diaries import views

app_name = 'diary board'
urlpatterns = [
    path('', views.diary, name='diary'),
]
