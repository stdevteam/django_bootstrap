from rest_framework import viewsets

from .models import Checkmarks
from .serializers import CheckmarksSerializer


class CheckmarksViewSet(viewsets.ModelViewSet):
    serializer_class = CheckmarksSerializer
    queryset = Checkmarks.objects.all()
