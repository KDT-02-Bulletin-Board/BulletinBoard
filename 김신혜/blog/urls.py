from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.PostList.as_view(), name='post_list'),
    path('<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
    # path('new/', views.new, name='new'),
    # path('create/', views.create, name='create'),
]
