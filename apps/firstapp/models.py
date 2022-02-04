from django.db import models

from django.contrib.auth.models import User

class Account(models.Model):

    ACCOUNT_FULL_NAME_MAX_LENGTH = 20

    user = models.OneToOneField(
        User,
        on_delete = models.CASCADE
    )
    full_name = models.CharField(
        max_length=ACCOUNT_FULL_NAME_MAX_LENGTH
    )
    description = models.TextField()

    def __str__(self) -> str:
        return f'Account: {self.user.id} / {self.full_name}' 

    class Meta:
        ordering = (
            'full_name',
        )
        verbose_name = 'Аккаунт'
        verbose_name_plural = 'Аккаунты'
