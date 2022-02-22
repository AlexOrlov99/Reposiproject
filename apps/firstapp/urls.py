
from . import views

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index_3),
    # path('admin/', views.index),
    # path('admin/show/', views.index_2),
    path('admin/', views.admin),
    path('show/', views.show),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
