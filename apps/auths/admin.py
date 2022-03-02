from django.contrib import admin

from . models import (
    CustomUser,
    )

class AccountAdmin(admin.ModelAdmin):
    readonly_fields = ()

    def get_readonly_fields(
        self,
        request: WSGIRequest,
        obj: Optional[Account] = None
    ) -> tuple:
        if obj:
            return self.readonly_fields + (
                'is_superuser',
                'is_staff',
                'username',
                'email',
                'password',
                )
        return self.readonly_fields
