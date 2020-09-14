from rest_framework import viewsets
from .serializers import DispatchSerializer
from .models import Dispatch
from rest_framework import permissions

class DispatchView(viewsets.ModelViewSet):
    queryset = Dispatch.objects.all()
    serializer_class = DispatchSerializer
    permission_classes = (permissions.AllowAny,)

    def perform_create(self, serializer):
        serializer.save()