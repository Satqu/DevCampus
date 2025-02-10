from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserProfileViewSet
from django.urls import path
from .views import home
from .views import index

router = DefaultRouter()
router.register(r'users', UserProfileViewSet)

urlpatterns = [
    path('', index, name='index'),
]