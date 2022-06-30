from django.urls import include, path
from rest_framework.routers import DefaultRouter

from users.views import CustomUserViewSet
from .views import (IngredientViewSet, RecipeViewSet, ShoppingCardView,
                    TagViewSet)

app_name = 'api'

router_v1 = DefaultRouter()
router_v1.register(r'users', CustomUserViewSet, basename='users')
router_v1.register(r'tags', TagViewSet, basename='tags')
router_v1.register(r'ingredients', IngredientViewSet, basename='ingredients')
router_v1.register(r'recipes', RecipeViewSet, basename='recipes')


urlpatterns = [
    path(
        'recipes/download_shopping_cart/',
        ShoppingCardView.as_view(),
        name='download_shopping_cart'
    ),
    path('', include(router_v1.urls)),
    path('auth/', include('djoser.urls.authtoken'))
]