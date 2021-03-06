
import names, random

from datetime import datetime

from logging import raiseExceptions

from django.core.management.base import BaseCommand
from django.conf import settings
# from django.contrib.auth.models import (
#     User,
# )

from auths.models import CustomUser

from django.contrib.auth.hashers import make_password

from firstapp.models import (
    Group,
    )


class Command(BaseCommand):
    """Custom command for filling up database.

    Test data only
    """
    help = 'Custom command for filling up database.'

    def init(self, *args: tuple, **kwargs: dict) -> None:
        pass

    def _generate_users(self) -> None:
        """Generate Users objs."""
        TOTAL_USERS_COUNT = 500
    
        def generate_password() -> str:
            _password_pattern: str = 'abcde12345'
            password: str = make_password(_password_pattern)
            return password

        def generate_email(first_name: str, last_name: str) -> str:
            
            _email_patterns: tuple = (
                'gmail.com', 'outlook.com', 'yahoo.com',
                'inbox.ru', 'inbox.ua', 'inbox.kz',
                'yandex.ru', 'yandex.ua', 'yandex.kz',
                'mail.ru', 'mail.ua', 'mail.kz',
                )
            domain_name: str = random.choice(_email_patterns)
            full_name: str = f'{first_name.lower()}.{last_name.lower()}'
            email: str = f'{full_name}@{domain_name}'
            return email

        def generate_username(first_name: str, last_name: str) -> str:
            username: str = f'{first_name.lower()}_{last_name.lower()}'
            return username

        if not CustomUser.objects.filter(is_superuser=True).exists():
            superuser: dict = {
                'is_superuser': True,
                'is_staff': True,
                'username': 'alex',
                'email': 'orlo.alex@mail.ru',
                'password': 'andromeda',
                'first_name': 'Alexey',
                'last_name': 'Orlov',
            }
            User.objects.create_superuser(**superuser)
        if CustomUser.objects.filter(
            is_superuser=False
            ).count()== TOTAL_USERS_COUNT:
            return

        _: int
        user_count: int = User.objects.count()
        for _ in range(TOTAL_USERS_COUNT - user_count):
            first_name: str = names.get_first_name()
            last_name: str = names.get_last_name()
            username : str= generate_username(first_name, last_name)
            email: str = generate_email(first_name, last_name)
            password: str = generate_password()
            CustomUser.objects.create(
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=password
            )

    def _generate_groups(self) -> None:
            """Generate Group objs."""

            def generate_name(inc: int) -> str:
                return f'???????????? {inc}'

            inc: int
            for inc in range(20):
                name: str = generate_name(inc)
                Group.objects.create(
                    name=name
                )

    # def _generate_students(self) -> None:
    #     """Generate Accounts and Students objs."""

    #     def generate_name(inc: int) -> str:
    #         return f'???????????? {inc}'

    #     inc: int
    #     for inc in range(20):
    #         name: str = generate_name(inc)
    #         Group.objects.create(
    #             name=name
    #         )

    def handle(self, *args: tuple, **kwargs: dict) -> None:
        """Handles data filling."""
        
        start: datetime = datetime.now()

        # self._generate_groups()
        self._generate_users()

        print(
            'Generating Data: {} seconds'.format(
                (datetime.now()-start).total_seconds()
            )
        )