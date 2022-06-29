from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework import filters, viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny

from recipes.models import Ingredient, Tag, Recipe, Favorite, Shopping
from .mixins import ListRetrieveViewSet
from .serializers import (IngredientSerializer,
                          TagSerializer,
                          RecipeGetSerializer,
                          RecipeSerializer,
                          RecipeFollowSerializer)
from .pagination import CustomPageNumberPagination
from .filters import RecipeFilter
from .permissions import IsAuthorOrReadOnly
from .utils import delete, post


class TagViewSet(ListRetrieveViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (AllowAny,)


class IngredientViewSet(ListRetrieveViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = (AllowAny,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('^name',)


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_class = RecipeFilter
    pagination_class = CustomPageNumberPagination

    def get_queryset(self):
        is_favorited = self.request.query_params.get("is_favorited")
        if is_favorited is not None and int(is_favorited) == 1:
            return Recipe.objects.filter(favorite__user=self.request.user)
        is_in_shopping_cart = self.request.query_params.get(
            "is_in_shopping_cart")
        if is_in_shopping_cart is not None and int(is_in_shopping_cart) == 1:
            return Recipe.objects.filter(shopping__user=self.request.user)
        return Recipe.objects.all()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response("Рецепт успешно удален",
                        status=status.HTTP_204_NO_CONTENT)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_serializer_class(self):
        if self.request.method == "GET":
            return RecipeGetSerializer
        return RecipeSerializer

    def get_permissions(self):
        if self.action != "create":
            return(IsAuthorOrReadOnly(),)
        return super().get_permissions()

    @action(detail=True, methods=["post", "delete"],)
    def favorite(self, request, pk):
        if self.request.method == "POST":
            return post(request, pk, Favorite, RecipeFollowSerializer)
        return delete(request, pk, Favorite)

    @action(detail=True, methods=["post", "delete"],)
    def shopping_cart(self, request, pk):
        if request.method == "POST":
            return post(request, pk, Shopping, RecipeFollowSerializer)
        return delete(request, pk, Shopping)
