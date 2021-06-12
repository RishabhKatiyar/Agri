from django.contrib import admin
from rest_framework.routers import DefaultRouter
from .views import NewsViewSet

router = DefaultRouter()
router.register(r'news', NewsViewSet, basename='student')

urlpatterns = router.urls