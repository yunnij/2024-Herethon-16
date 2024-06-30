from django.contrib import admin
from .models import Role, Portfolio, Career

class RoleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('role',)}

admin.site.register(Role)
admin.site.register(Portfolio)
admin.site.register(Career)