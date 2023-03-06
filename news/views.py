from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status, filters, generics, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from custom_auth.jwt import JWTAuthentication
from .pagination import CustomPageNumberPagination
from .permissions import AuthorAllStaffAll, SAFE_METHODS
from .serializers import *


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    pagination_class = CustomPageNumberPagination
    # authentication_classes = [JWTAuthentication]  # IsAdminUser]
    permission_classes = [AuthorAllStaffAll]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    filterset_fields = ['author', 'timestamp']
    search_fields = ['id', 'title', 'author', 'text']
    ordering_fields = ['id', 'author', 'timestamp', 'likes']

    def create(self, request, *args, **kwargs):
        serializer = NewsSerializer(data=request.data)  # omit author & likes

        if serializer.is_valid():
            serializer.save(author=self.request.user)
            return Response(serializer.data)

    # def get_serializer_class(self):
    #     if self.action == 'list':
    #         return serializers.ListaGruppi
    #     if self.action == 'retrieve':
    #         return serializers.DettaglioGruppi
    #     return NewsSerializer

    # [+]
    def get_serializer_class(self):
        if self.request.method not in SAFE_METHODS:  # == 'POST'
            return PostNewsSerializer
        else:
            return NewsSerializer
