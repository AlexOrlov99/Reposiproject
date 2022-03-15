from django.contrib.auth.models import (
    AbstractBaseUser, 
    PermissionsMixin,
)
from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import ValidationError


class CustomUserManager(BaseUserManager):

    def create_user(
        self, 
        email: str, 
        password: str, 
        **kwargs: dict
        ) -> 'CustomUser':

        if not email:
            raise ValidationError('Email required')

        email: str = self.normalize_email(email)
        user: CustomUser = self.model(
            email=email,
            **kwargs
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(
        self,
        email: str,
        password: str,
        **kwargs: dict
    ) -> 'CustomUser':
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_root', True)

        if kwargs.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        if kwargs.get('is_root') is not True:
            raise ValueError('Superuser must have is_root=True')

        user: 'Customer' =  self.create_user(
            email,
            password,
            **kwargs
        )
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('Почта/Логин', unique=True)
    is_root = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    datatime_joined = models.DateTimeField(
        verbose_name='Время регистрации',
        auto_now_add=True
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self) -> str:
        return f'User{self.email}, {self.is_root}, \
        {self.is_staff}, {self.datatime_joined}'


    def save(self,
        *args: tuple,
        **kwargs: dict
        ) -> None:
        if self.email is not self.email.lower():
            raise ValidationError(
                f'{self.email} - invalid'
            )
            
    class Meta:
        ordering = (
            'email',
            'is_root',
            'is_staff',
            'datatime_joined',
        )
        verbose_name = 'Пользователь'
        verbose_name = 'Пользователи'