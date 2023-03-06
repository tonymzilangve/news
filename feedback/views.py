from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.response import Response

from news.pagination import CustomPageNumberPagination
from news.permissions import AuthorAllStaffAllButEdit
from .serializers import *
from .models import *


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    pagination_class = CustomPageNumberPagination
    # authentication_classes = [JWTAuthentication]
    permission_classes = [AuthorAllStaffAllButEdit]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    filterset_fields = ['author', 'timestamp']
    search_fields = ['id', 'title', 'author', 'text']
    ordering_fields = ['id', 'author', 'timestamp', 'likes']

    def create(self, request, *args, **kwargs):
        serializer = CommentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(author=self.request.user)
            return Response(serializer.data)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return PostCommentSerializer
        else:
            return CommentSerializer
