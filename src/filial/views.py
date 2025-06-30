from rest_framework import viewsets
from .models import Filial
from .serializers import FilialSerializer


class FilialViewSet(viewsets.ModelViewSet):
    queryset = Filial.objects.all()
    serializer_class = FilialSerializer
