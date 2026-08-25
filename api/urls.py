from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, ServiceViewSet

router = DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'services', ServiceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
