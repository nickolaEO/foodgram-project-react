from rest_framework import mixins, viewsets
from rest_framework.permissions import AllowAny

from recipes.models import Tag

from .serializers import TagSerializer


class TagViewSet(mixins.RetrieveModelMixin,
                 mixins.ListModelMixin,
                 viewsets.GenericViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (AllowAny,)
