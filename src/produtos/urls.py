from rest_framework.routers import DefaultRouter
from .views import AlimentacaoViewSet, VestuarioViewSet, UtilidadesDomesticasViewSet

router = DefaultRouter()
router.register(r'alimentacao', AlimentacaoViewSet)
router.register(r'vestuario', VestuarioViewSet)
router.register(r'utilidades-domesticas', UtilidadesDomesticasViewSet)

urlpatterns = router.urls
