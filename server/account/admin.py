from django.contrib import admin

from account.models import Account, DummyUser

# Register your models here.


admin.site.register(Account)
admin.site.register(DummyUser)
