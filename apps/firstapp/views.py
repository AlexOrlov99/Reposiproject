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


class IndexView(View):

    def get(self,
        request: WSGIRequest,
        *args: tuple,
        **kwargs
    ):
        return HttpResponse('Hello, World!')


def index(request: WSGIRequest) -> HttpResponse:

    if not request.user.is_authenticated:
        return render(
            request,
            'firstapp/login.html'
        )
    homeworks: QuerySet = Homework.objects.filter(
        user=request.user
    )
    context: dict = {
        'ctx_title': 'Главная страница',
        'ctx_homeworks': homeworks,
    }
    return render(
        request,
        template_name='firstapp/main.html',
        context=context
    )

def index_2(request: WSGIRequest) -> HttpResponse:
    return HttpResponse(
        '<h1>Page: Start</h1>'
    )

def admin(request: WSGIRequest) -> HttpResponse:
    context: dict = {
        'ctx_title': 'Главная страница',
        'ctx_users': CustomUser.objects.all(),
    }
    
    return render(
        request,
        'firstapp/admin.html',
        context
    )

def show(request: WSGIRequest, user_id: str) -> HttpResponse:
    user = CustomUser.objects.get(id=user_id)
    context: dict = {
        'ctx_title': 'Профиль пользователя',
        'ctx_user': user,
    }
    return render(
        request,
        'firstapp/show.html',
        context
    )

def delete(request: WSGIRequest) -> HttpResponse:

 return HttpResponse(
        '<h1>Page: Delete</h1>'
    )

def register(request: WSGIRequest) -> HttpResponse:

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
            return render(
                request,
                'firstapp/main.html',
                {'homeworks': homeworks}
            )
    context: dict = {
        'form': form
    }
    return render(
        request,
        'firstapp/register.html',
        context
    )

def login(request: WSGIRequest) -> HttpResponse:

    if request.method == 'POST':
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
        return render(
            request,
            'firstapp/main.html',
            {'homeworks': homeworks}
        )
    return render(
        request,
        'firstapp/login.html'
    )

def logout(request: WSGIRequest) -> HttpResponse:

    dj_logout(request)

    form: CustomUserForm = CustomUserForm(
        request.POST
    )
    context: dict = {
        'form': form,
    }
    return render(
        request,
        'firstapp/login.html',
        context
    )