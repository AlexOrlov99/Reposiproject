<<<<<<< HEAD

import names, random

=======
import names
import random
>>>>>>> 063c47157c6f46bdcea71029a61eb700f466d1b0
from typing import Any
from datetime import datetime

from logging import raiseExceptions

from django.core.management.base import BaseCommand
from django.conf import settings
from django.contrib.auth.models import (
    User,
)
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
<<<<<<< HEAD
        MAX_SUPERUSER_COUNT = 1
        TOTAL_USERS_COUNT = 500

        def generate_username() -> str:


=======
        TOTAL_USERS_COUNT = 500

        def generate_first_name()-> str:
            first_name: str = names.get_first_name()
            return first_name
        
        def generate_last_name() -> str:
            last_name: str = names.get_last_name()
            return last_name
        
>>>>>>> 063c47157c6f46bdcea71029a61eb700f466d1b0
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
<<<<<<< HEAD
            full_name: str = f'{first_name.lower()}.{last_name.lower()}'
            email: str = f'{full_name}@{domain_name}'
            return email
            
        user_count = len(user_list)
        if not User.objects.filter(is_superuser='True').exists()
            User.objects.create(
                is_superuser='True',
                is_staff='True',
                username='alex',
                email='orlo_alex@mail.ru',
                password='andromeda',
                first_name='Alex',
                last_name='Orlov',
                )

        inc: int
        for inc in range(TOTAL_USERS_COUNT-MAX_SUPERUSER_COUNT-user_count):
            first_name: str = names.get_first_name()
            last_name: str = names.get_last_name()
            username : str= f'{first_name.lower()}_{last_name.lower()}'
=======
            full_name: str = first_name.lower() + '.' + last_name.lower()
            email: str = full_name + '@' + domain_name
            return email

        def generate_username(first_name: str, last_name: str) -> str:
            username: str = first_name.lower()  + '_' + last_name.lower() 
            return username
            
        inc: int
        user_count: int = User.objects.count()
        for inc in range(TOTAL_USERS_COUNT - user_count):
            first_name: str = generate_first_name()
            last_name: str = generate_last_name()
            username : str= generate_username(first_name, last_name)
>>>>>>> 063c47157c6f46bdcea71029a61eb700f466d1b0
            email: str = generate_email(first_name, last_name)
            password: str = generate_password()
            User.objects.create(
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=password
            )

<<<<<<< HEAD
# def _generate_groups(self) -> None:
    #     """Generate Group objs."""

    #     def generate_name(inc: int) -> str:
    #         return f'Группа {inc}'

    #     inc: int
    #     for inc in range(20):
    #         name: str = generate_name(inc)
    #         Group.objects.create(
    #             name=name
    #         )

    # def _generate_accounts_and_students(self) -> None:
    #     """Generate Accounts and Students objs."""
=======
    # def _generate_groups(self) -> None:
    #     """Generate Group objs."""
>>>>>>> 063c47157c6f46bdcea71029a61eb700f466d1b0

    #     def generate_name(inc: int) -> str:
    #         return f'Группа {inc}'

    #     inc: int
    #     for inc in range(20):
    #         name: str = generate_name(inc)
    #         Group.objects.create(
    #             name=name
    #         )

    def handle(self, *args: tuple, **kwargs: dict) -> None:
        """Handles data filling."""
        
        start: datetime = datetime.now()

<<<<<<< HEAD
        # self._generate_groups()
        self._generate_users()
=======

        self._generate_users()

        #print(self.temp())
>>>>>>> 063c47157c6f46bdcea71029a61eb700f466d1b0

        print(
            'Generating Data: {} seconds'.format(
                (datetime.now()-start).total_seconds()
            )
        )