from rest_framework import filters
from rest_framework.permissions import AllowAny

from recipes.models import Ingredient, Tag
from .mixins import ListRetrieveViewSet
from .serializers import IngredientSerializer, TagSerializer


class TagViewSet(ListRetrieveViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (AllowAny,)


class IngredientViewSet(ListRetrieveViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = (AllowAny,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
