from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model

# from .forms import CustomUserCreationForm, CustomUserChangeForm
User = get_user_model()


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    list_display = ['username', 'date_joined', 'is_staff', 'is_superuser']
