from django.contrib import admin
from .models import *
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User


admin.site.register(Posts)
admin.site.register(Day)
admin.site.register(Object)
admin.site.register(Messages)


