
from . import views

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from firstapp.views import (
    IndexView,
    )


urlpatterns = [
    path('',                    IndexView.as_view(), name='page_main'),
    path('admin/',              views.admin),
    path('show/<int:user_id>/', views.show,          name='page_show'),
    path('delete/',              views.delete,       name='page_delete'),
    path('register/',            views.register,     name='page_register'),
    path('login/',               views.login,        name='page_login'),
    path('logout/',              views.logout,       name='page_logout'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
