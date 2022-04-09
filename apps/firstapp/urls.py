from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from firstapp.views import (
    IndexView,
    ShowView,

    RegisterView,
    LoginView,
    LogoutView,

    HomeworkDetailView,
    HomeworkCreateView,
    HomeworkDeleteView,

    HomeworkFilesCheckView,
    HomeworkFilesDeleteView,
    HomeworkFilesView,
    HomeworkFilesCreateView,
    )


urlpatterns = [
    path(
        '', 
        IndexView.as_view(),
        name='page_main'
    ),
    path(
        'show/<int:homework_id>/',
        ShowView.as_view(),
        name='page_show'
    ),

    # ------------------------------------------------------|
    # Auths
    #
    path(
        'register/',
        RegisterView.as_view(),
        name='page_register'
    ),
    path(
        'login/',
        LoginView.as_view(),
        name='page_login'
    ),
    path(
        'logout/',
        LogoutView.as_view(),
        name='page_logout'
    ),

    # ------------------------------------------------------|
    # Homework
    #
    path(
        'homework_detail/<int:homework_id>/',
        HomeworkDetailView.as_view(),
        name='page_homework_detail'
    ),
    path(
        'homework_create/',
        HomeworkCreateView.as_view(),
        name='page_homework_create'
    ),
    path(
        'homeowrk_delete/<int:homework_id>/',
        HomeworkDeleteView.as_view(),
        name='page_homework_delete'
    ),

    # ------------------------------------------------------|
    # Files
    #   
    path(
        'homework_files/<str:filter_by>',
        HomeworkFilesView.as_view(),
        name='page_homework_files'
    ),
    path(
        'homework_files/<int:homework_id>',
        HomeworkFilesCreateView.as_view(),
        name='page_homework_files_create'
    ),
    path(
        'homework_files_check/<int:file_id>',
        HomeworkFilesCheckView.as_view(),
        name='page_homework_files_check'
    ),
    path(
        'homework_files_delete/<int:file_id>',
        HomeworkFilesDeleteView.as_view(),
        name='page_homework_files_delete'
    ),    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
