from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/', views.blog, name='blog'),
    path('blog/<int:num>/', views.posting, name='posting'),
    path('blog/new_post/', views.new_post),
    path('blog/<int:num>/remove', views.remove_post),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)