from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'comments', CommentViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
