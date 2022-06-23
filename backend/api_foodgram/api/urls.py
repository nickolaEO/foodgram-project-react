from django.urls import include, path
from rest_framework.routers import DefaultRouter

from users.viewsets import CustomUserViewSet


app_name = 'api'

router = DefaultRouter()
router.register(r'users', CustomUserViewSet, basename='users')


urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls.authtoken'))
]
