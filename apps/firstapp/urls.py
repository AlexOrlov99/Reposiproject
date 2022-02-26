
from . import views

from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index_3),
    path('admin/', views.admin),
    re_path(r'^show/(?P<username>\w+)/$', views.show, name='page_show'),
    path('delete', views.delete, name='page_delete')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
