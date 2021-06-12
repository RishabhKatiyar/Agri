from .models import News
from .serializers import NewsSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.status import HTTP_409_CONFLICT
import random

class NewsViewSet(viewsets.ModelViewSet):
    serializer_class = NewsSerializer
    queryset = News.objects.all()

    def list(self, request, *args, **kwargs):
        rand= random.randrange(start=1, stop=10)
        if not rand % 5 == 0:
            return Response(status = HTTP_409_CONFLICT)
        return super().list(self, request, args, kwargs)