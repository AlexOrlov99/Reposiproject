from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.contrib.auth.models import User

from firstapp.models import (
    Account,
    Group,
    Student,
    Professor,
)



def index(request: WSGIRequest) -> HttpResponse:
    """Searh first user"""

    student: Student = Student.objects.first()
    gpa: int = student.gpa
    
    account: Account = student.account
    name_acc: str = account.full_name

    user: User = account.user
    name: str = user.first_name

    text: str = f'''<h1>Username: {name}<br> Account: {name_acc}<br>
                        GPA: {gpa}</h1>
                '''

    response: HttpResponse = HttpResponse(text)
    return response

def index_2(request: WSGIRequest) -> HttpResponse:
    return HttpResponse(
        '<h1>Page: Start</h1>'
    )