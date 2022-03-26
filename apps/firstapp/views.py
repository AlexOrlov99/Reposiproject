from multiprocessing import context
from re import template
from django.db.models import QuerySet
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.contrib.auth import (
    authenticate as dj_authenticate,
    login as dj_login,
    logout as dj_logout,
)
from django import forms
from django.shortcuts import render
from apps.auths.forms import CustomUserForm

from auths.models import CustomUser

from firstapp.models import (
    Group,
    Student,
    Professor,
    Homework
)
from django.views import View
from django.template import loader


class IndexView(View):

    def get(self,
        request: WSGIRequest,
        *args: tuple,
        **kwargs: dict,
        ) -> HttpResponse:

        if not request.user.is_authenticated:
            return render(
                request,
                'firstapp/login.html'
                )
        homeworks: QuerySet = Homework.objects.filter(
            user=request.user,
            is_checked=False,
            )
        context: dict = {
            'ctx_title': 'Главная страница',
            'ctx_homeworks': homeworks,
            }
        template_name = loader.get_template(
            'firstapp/main.html'
        )
        return HttpResponse(
            template_name.render(
                context, request
            ),
            content_type='text/html'
        )


class AdminView(View):

    def get(self,
        request: WSGIRequest,
        *args: tuple,
        **kwargs: dict,
        ) -> HttpResponse:

        context: dict = {
            'ctx_title': 'Главная страница',
            'ctx_users': CustomUser.objects.all(),
            }
        template_name = loader.get_template(
            'firstapp/admin.html'
        )
        return HttpResponse(
            template_name.render(
                context, request
            ),
            content_type='text/html'
        )        


class ShowView(View):

    def get(self,
        request: WSGIRequest,
        user_id: str,
        *args: tuple,
        **kwargs: dict,
        ) -> HttpResponse:
        
        user = CustomUser.objects.get(id=user_id)
        context: dict = {
            'ctx_title': 'Профиль пользователя',
            'ctx_user': user,
            }
        template_name = loader.get_template(
            'firstapp/show.html'
        )
        return HttpResponse(
            template_name.render(
                context, request
            ),
            content_type='text/html'
        )


class DeleteView(View):

    def get(self,
        request: WSGIRequest,
        user_id: str,
        *args: tuple,
        **kwargs: dict,
        ) -> HttpResponse:

        user = CustomUser.objects.get(id=user_id)
        user.delete()

        context: dict = {
            'ctx_title': 'Главная страница',
            'ctx_users': CustomUser.objects.all(),
            }
            
        template_name = loader.get_template(
            'firstapp/admin.html'
        )
        return HttpResponse(
            template_name.render(
                context, request
            ),
            content_type='text/html'
            )


class RegisterView(View):

    def get(self,
        request: WSGIRequest,
        *args: tuple,
        **kwargs
        ) -> HttpResponse:

        form: CustomUserForm = CustomUserForm(
            request.POST
            )
        context: dict = {
            'form': form
        }        
        template_name = loader.get_template(
            'firstapp/register.html'
        )
        return HttpResponse(
            template_name.render(
                context, request
            ),
            content_type='text/html'
        )

    def post(self,
        request: WSGIRequest,
        *args: tuple,
        **kwargs
        ) -> HttpResponse:

        form: CustomUserForm = CustomUserForm(
            request.POST
            )        
        if form.is_valid():
            user: CustomUser = form.save(
                commit=False
            )
            email: str = form.cleaned_data['email']
            password: str = form.cleaned_data['password']
            user.email = email
            user.set_password(password)
            user.save()
            user: CustomUser = dj_authenticate(
                email=email,
                password=password
            )
            if user and user.is_active:
                dj_login(request, user)

                homeworks: QuerySet = Homework.objects.filter(
                    user=request.user
                )
                context: dict = {
                    'homeworks':homeworks
                }
                template_name = loader.get_template(
                    'firstapp/main.html'
                )
                return HttpResponse(
                    template_name.render(
                        context, request
                    ),
                    content_type='text/html'
                )


class LoginView(View):

    def get(self,
        request: WSGIRequest,
        *args: tuple,
        **kwargs
        ) -> HttpResponse:

        form: CustomUserForm = CustomUserForm(
            request.POST
            )
        context: dict = {
            'form': form
        }        
        template_name = loader.get_template(
            'firstapp/login.html'
        )
        return HttpResponse(
            template_name.render(
                context, request
            ),
            content_type='text/html'
        )

    def post(self,
        request: WSGIRequest,
        *args: tuple,
        **kwargs
        ) -> HttpResponse:
        email: str = request.POST['email']
        password: str = request.POST['password']

        user: CustomUser = dj_authenticate(
            email=email,
            password=password
        )
        if not user:
            return render(
                request,
                'firstapp/login.html',
                {'error_message': 'Невереные данные'}
            )
        if not user.is_active:
            return render(
                request,
                'firstapp/login.html',
                {'error_message': 'Ваш аккаунт был удален'}
            )
           
        dj_login(request, user)
        homeworks: QuerySet = Homework.objects.filter(
            user=request.user,
            is_checked=False,
        )
        context: dict = {
            'homeworks': homeworks
        }
        template_name = loader.get_template(
            'firstapp/main.html'
        )        
        return HttpResponse(
            template_name.render(
                context, request
            ),
            content_type='text/html'
        )


class LogoutView(View):

    def get(self,
        request: WSGIRequest,
        *args: tuple,
        **kwargs
        ) -> HttpResponse:

        dj_logout(request)

        form: CustomUserForm = CustomUserForm(
            request.POST
            )
        context: dict = {
            'form': form,
            }
        template_name = loader.get_template(
            'firstapp/login.html'
        )       
        return HttpResponse(
            template_name.render(
                context, request
            ),
            content_type='text/html'
        )