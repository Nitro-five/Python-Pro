from django.contrib import admin
from .models import MyModel, AnotherModel, CustomUser

# Админка для MyModel
class MyModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    list_filter = ('name',)

# Админка для AnotherModel
class AnotherModelAdmin(admin.ModelAdmin):
    list_display = ('name',)

# Админка для CustomUser
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'phone_number')
    search_fields = ('username',)

# Регистрируем модели с админскими классами
admin.site.register(AnotherModel, AnotherModelAdmin)
admin.site.register(MyModel, MyModelAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
