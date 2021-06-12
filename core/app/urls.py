from django.urls.conf import path
from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter
from .views import NewsView


#router = DefaultRouter()
#router.register(r'student', NewsView, basename='student')

#urlpatterns = router.urls


urlpatterns = [
    path('news/', NewsView.as_view({
        'get':'list'
    }), name='student')
]