
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import User, Profile

class UserAdmin(BaseUserAdmin):
  fieldsets = (
      (None, {'fields': ('email', 'password', )}),
  )
  add_fieldsets = (
      (None, {
          'classes': ('wide', ),
          'fields': ('email', 'password1', 'password2'),
      }),
  )
  list_display = ['email', ]
  search_fields = ('email', )
  ordering = ('email', )

admin.site.register(User, UserAdmin)
admin.site.register(Profile)