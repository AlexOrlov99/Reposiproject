
from . import views

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from firstapp.views import (
    IndexView,
    HomeworkCreateView,
    HomeworkDetailsView,
    AdminView,
    ShowView,
    DeleteUserView,
    RegisterView,
    LoginView,
    LogoutView,

    )


urlpatterns = [
    path('',                            IndexView.as_view(),            name='page_main'            ),
    path('create/',                     HomeworkCreateView.as_view(),   name='page_homework_create' ),
    path('detail/<int:homework_id>/',   HomeworkDetailsView.as_view(),  name='page_homework_detail' ),
    path('admin/',                      AdminView.as_view()                                         ),
    path('show/<int:homework_id>/',     ShowView.as_view(),             name='page_show'            ),
    path('delete/<int:user_id>/',       DeleteUserView.as_view(),       name='page_delete'          ),
    path('register/',                   RegisterView.as_view(),         name='page_register'        ),
    path('login/',                      LoginView.as_view(),            name='page_login'           ),
    path('logout/',                     LogoutView.as_view(),           name='page_logout'          ),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
