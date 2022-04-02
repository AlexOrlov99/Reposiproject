from typing import Optional
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
from apps.firstapp.forms import HomeworkForm

from auths.models import CustomUser

from firstapp.models import (
    Group,
    Student,
    Professor,
    Homework,
)
from django.views import View
from django.template import loader
from abstracts.mixins import HttpResponseMixin
from abstracts.handlers import ViewHandler


class IndexView(ViewHandler, View):

    template_name: str = 'firstapp/main.html'

    def get(self,
        request: WSGIRequest,
        *args: tuple,
        **kwargs: dict,
        ) -> HttpResponse:

        response: Optional[HttpResponse] = \
            self.get_validated_response(
                request
            )
        if response:
            return response
            
        homeworks: QuerySet = Homework.objects.filter(
            user=request.user,
            )
        
        context: dict = {
            'ctx_title': 'Главная страница',
            'ctx_homeworks': homeworks,
            }
    
        return self.get_http_response(
            request,
            self.template_name,
            context
        )


class HomeworkDetailsView(ViewHandler, View):

    queryset: QuerySet = Homework.objects.get_not_deleted()

    template_name: str ='firstapp/homework_detail.html'    

    def get(
        self,
        request: WSGIRequest,
        *args: tuple,
        **kwargs: dict
        ) -> HttpResponse:
        
        homework = self.queryset.filter(user=self.request.user)

        context: dict = {
            'homework': homework
        }
        print(context)
        return self.get_http_response(
            request,
            self.template_name,
            context
            )        


class HomeworkCreateView(ViewHandler, View):

    form: HomeworkForm = HomeworkForm
    template_name: str = 'firstapp/homework_create.html'    

    def get(
        self,
        request: WSGIRequest,
        *args: tuple,
        **kwargs: dict
        ) -> HttpResponse:
        """GET request handler."""

        response: Optional[HttpResponse] = \
            self.get_validated_response(
                request
            )
        if response:
            return response

        context: dict = {
            'ctx_form': self.form,
            }
        return self.get_http_response(
            request,
            self.template_name,
            context
            )       
    
    def post(self,
        request: WSGIRequest,
        *args: tuple,
        **kwargs
        ) -> HttpResponse:

        _form: HomeworkForm = self.form(
            request.POST or None,
            request.FILES or None
            )
        if not _form.is_valid():
            context: dict = {
                'ctx_form': _form,
                }
            return self.get_http_response(
                request,
                self.template_name,
                context
                )            
        homework: Homework = _form.save(
            commit=False
            )
        homework.user = request.user
        homework.logo = request.FILES['logo']

        file_type: str = homework.logo.url.split('.')[-1].lower()

        if file_type not in Homework.IMAGE_TYPES:

            context: dict = {
                'ctx_form': _form,
                'ctx_homework': homework,
                'error_message': 'PNG, JPG, JPEG',
                }
            return self.get_http_response(
                request,
                self.template_name,
                context
                )
        homework.save()

        context: dict = {
            'homework': homework
        }
        return self.get_http_response(
            request,
            'firstapp/homework_detail.html',
            context
            )                                        


class HomeworkFilesView(ViewHandler, View):
    pass


class AdminView(ViewHandler, View):
    
    template_name: str = 'firstapp/admin.html'
    
    def get(self,
        request: WSGIRequest,
        *args: tuple,
        **kwargs: dict,
        ) -> HttpResponse:

        users: QuerySet = CustomUser.objects.filter(
            is_active=True
        )
        context: dict = {
            'ctx_title': 'Главная страница',
            'ctx_users': users,
            }

        
        
        return self.get_http_response(
            request,
            self.template_name,
            context
        )     


class ShowView(ViewHandler, View):

    queryset: QuerySet = Homework.objects.get_not_deleted()

    template_name: str ='firstapp/show.html'

    def get(self,
        request: WSGIRequest,
        *args: tuple,
        **kwargs: dict,
        ) -> HttpResponse:
        homework_id: int = kwargs.get('homework_id', 0)
        
        # user = CustomUser.objects.get(id=user_id)
        homework: Optional[Homework] = None

        try:
            homework = self.queryset.filter(user=self.request.user)\
                .get(id=homework_id)

        except Homework.DoesNotExist:
            return self. get_http_response(
                request,
                'firstapp/login.html'
                )
        else:
            context: dict = {
                'ctx_title': 'Профиль пользователя',
                'ctx_homework': homework,
                }
        
        return self.get_http_response(
            request,
            self.template_name,
            context
        )


class DeleteUserView(ViewHandler, View):

    template_name: str = 'firstapp/admin.html'

    def get(self,
        request: WSGIRequest,
        user_id: int,
        *args: tuple,
        **kwargs: dict,
        ) -> HttpResponse:

        user = CustomUser.objects.get(id=user_id)
        print(user)
        user.delete()
        

        context: dict = {
            'ctx_title': 'Главная страница',
            'ctx_users': CustomUser.objects.all(),
            }
            
        return self.get_http_response(
            request,
            self.template_name,
            context
        )    


class RegisterView(ViewHandler, View):

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
        template_name = 'firstapp/register.html'
        
        return self.get_http_response(
            request,
            template_name,
            context
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
                template_name: str = 'firstapp/main.html'
                
                return self.get_http_response(
                    request,
                    template_name,
                    context
                )


class LoginView(ViewHandler, View):

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
        
        template_name: str = 'firstapp/login.html'
        
        return self.get_http_response(
            request,
            template_name,
            context
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
            user=request.user
        )
        context: dict = {
            'homeworks': homeworks
        }
       
        template_name: str = 'firstapp/main.html'
        
        return self.get_http_response(
            request,
            template_name,
            context
        )


class LogoutView(ViewHandler, View):

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
  
        template_name: str = 'firstapp/login.html'

        return self.get_http_response(
            request,
            template_name,
            context
        )