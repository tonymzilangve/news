from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'news', NewsViewSet)


urlpatterns = [
    path('', include(router.urls)),
]