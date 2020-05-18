from .models import Request
from rest_framework import viewsets, permissions
from .serializers import RequestSerializer


class RequestViewSet(viewsets.ModelViewSet):
    queryset = Request.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = RequestSerializer
