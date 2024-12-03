from django.contrib import admin
from .models import *

# Админка для Buyer
@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display = ('name', 'balance', 'age')
    search_fields = ('name',)


# Админка для Games
@admin.register(Games)
class GamesAdmin(admin.ModelAdmin):
    list_display = ('title', 'cost', 'size', 'description', )
    search_fields = ('title', )
    list_filter = ('cost', )
    list_per_page = 5  # количество игр на странице
    # Разбивка на секции
    fieldsets = (
        (None, {
            'fields': ('title', 'cost', 'description')
        }),

        ('Дополнительные настройки', {
            'classes': ('collapse',), # скрытие секции по умолчанию
            'fields': ('size', 'age_limited')
        }),
    )

