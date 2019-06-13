from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import UserCreationForm, UserChangeForm
from .models import User


class UserAdmin(UserAdmin):
    model = User
    add_form = UserCreationForm
    form = UserChangeForm
    ordering = ('email',)


admin.site.register(User, UserAdmin)