from django.contrib import admin

from .models import SignUp
from .foreign_key import TestForeignkey

admin.site.register(SignUp)
admin.site.register(TestForeignkey)
