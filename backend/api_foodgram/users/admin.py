from django.contrib import admin

from api_foodgram.settings import EMPTY_VALUE_DISPLAY

from recipes.models import Tag, Ingredient, Recipe
from .models import CustomUser
from .forms import CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name'
    )
    search_fields = (
        'username',
        'email',
        'first_name',
        'last_name',
    )
    list_filter = ('email', 'username',)
    ordering = ('id',)
    empty_value_display = EMPTY_VALUE_DISPLAY


class TagAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'color',
        'slug'
    )
    search_fields = (
        'name',
        'color',
        'slug'
    )
    list_filter = ('name', 'color', 'slug',)
    ordering = ('name',)
    empty_value_display = EMPTY_VALUE_DISPLAY


class IngredientAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'measurement_unit'
    )
    search_fields = (
        'name',
        'measurement_unit'
    )
    list_filter = ('name',)
    ordering = ('name',)
    empty_value_display = EMPTY_VALUE_DISPLAY


class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'author'
    )
    search_fields = (
        'username',
        'email',
        'first_name',
        'last_name',
    )
    list_filter = ('author', 'name', 'tags',)
    ordering = ('name',)
    empty_value_display = EMPTY_VALUE_DISPLAY


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
