from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Mini Mercado API",
        default_version='v1',
        description="Documentação da API do Mini Mercado",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
