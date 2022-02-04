from typing import Optional
from django.contrib import admin
from django.core.handlers.wsgi import WSGIRequest
# Register your models here.
from . models import Account

class AccountAdmin(admin.ModelAdmin):
    readonly_fields = ()

    def get_readonly_fields(
        self,
        request: WSGIRequest,
        obj: Optional[Account] = None
    ) -> tuple:
        if obj:
            return self.readonly_fields + ('description',)
        return self.readonly_fields
admin.site.register(
    Account,AccountAdmin
)