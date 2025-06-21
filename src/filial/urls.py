from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FilialViewSet

router = DefaultRouter()
router.register(r'filiais', FilialViewSet)

urlpatterns = router.urls
