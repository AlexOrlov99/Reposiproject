from django.db.models import QuerySet
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render

from auths.models import CustomUser

from firstapp.models import (
    Group,
    Student,
    Professor,
)


def index(request: WSGIRequest) -> HttpResponse:
    """Searh first user"""

    student: Student = Student.objects.first()
    gpa: int = student.gpa
    
    # account: Account = student.account
    # name_acc: str = account.full_name

    # user: User = account.user
    # name: str = user.first_name
    customuser : CustomUser
    login : CustomUser.email


    # text: str = f'''<h1>Username: {name}<br> Account: {name_acc}<br>
    #                     GPA: {gpa}</h1>
                # '''
    text: str = f'''<h1>Login : {login}>
                '''

    response: HttpResponse = HttpResponse(text)
    return response

def index_2(request: WSGIRequest) -> HttpResponse:
    return HttpResponse(
        '<h1>Page: Start</h1>'
    )

def index(request: WSGIRequest) -> HttpResponse:
    users: QuerySet = CustomUser.objects.all()
    context: dict = {
        'ctx_title': 'Главная страница',
        'ctx_users': users,
    }
    return render(
        request,
        'index.html',
        context,
    )
def admin(request: WSGIRequest) -> HttpResponse:
    context: dict = {
        'ctx_title': 'Главная страница',
        'ctx_users': CustomUser.objects.all(),
    }
    
    return render(
        request,
        'admin.html',
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
        'show.html',
        context
    )
def delete(request: WSGIRequest) -> HttpResponse:

 return HttpResponse(
        '<h1>Page: Delete</h1>'
    )